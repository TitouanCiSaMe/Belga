"""
Parseur Format A — Annuaires 1995-1999.

Layout : 2 colonnes, numéro de carte sur la même ligne que le nom,
contacts simples (téléphones inline, pas de labels).
"""
import re
from .base import BaseParser
from ..constants import (
    CARTE_INLINE_RE, CP_VILLE_RE, NAME_BLACKLIST_STARTS,
    VOIR_RE, SKIP_HEADERS, STATUTS, EMAIL_RE, PHONE_RE,
)
from ..text_utils import clean_ocr_icons, fix_spacing, split_nom_prenom, clean_prenom
from ..models import new_fiche


class FormatAParser(BaseParser):
    format_id   = 'a'
    description = "1995-1999 — 2 colonnes, carte inline, contacts simples"
    is_default  = True  # Repli si aucun autre format n'est détecté

    def detect_page(self, page_text: str) -> bool:
        return False  # Format de repli : jamais détecté en positif

    def _detect_name(self, line: str):
        """Retourne (nom, prenom, carte) ou None."""
        m = CARTE_INLINE_RE.search(line)
        if not m:
            return None
        carte = m.group()
        name_part = line[:m.start()].strip()
        if not name_part or len(name_part) < 3:
            return None
        name_part = clean_ocr_icons(name_part)
        words = name_part.split()
        if len(words) < 2:
            return None
        first = re.sub(r'[^A-Za-zÉÈÊËÀÂÙÛÜÔÏÎéèêëàâùûüôïî\-\'\(\)]', '', words[0])
        if not first or not first[0].isupper():
            return None
        if NAME_BLACKLIST_STARTS.match(name_part):
            return None
        nom, prenom = split_nom_prenom(name_part)
        return nom, prenom, carte

    def parse(self, lines: list[str], debug: bool = False) -> list[dict]:
        fiches, current, phase = [], None, 'waiting'

        for raw_line in lines:
            line = clean_ocr_icons(fix_spacing(raw_line.strip()))
            if not line or line in SKIP_HEADERS or re.match(r'^\d{1,3}$', line):
                continue
            if VOIR_RE.match(line):
                if debug:
                    print(f"  [SKIP renvoi] {line}")
                continue
            if debug:
                print(f"  [{phase:12s}] {line}")

            parsed = self._detect_name(line)
            if parsed:
                if current and current['nom']:
                    fiches.append(current)
                nom, prenom, carte = parsed
                current = new_fiche(nom=nom, prenom=clean_prenom(prenom), carte_presse=carte)
                phase = 'got_name'
                continue

            if not current:
                continue

            m_cp = CP_VILLE_RE.match(line)
            if m_cp and phase in ('got_name', 'got_addr'):
                current['code_postal'] = m_cp.group(1)
                ville = m_cp.group(2).strip()
                cp2 = re.search(r'\s+\d{4}\s+', ville)
                if cp2:
                    ville = ville[:cp2.start()].strip()
                current['ville'] = ville
                phase = 'got_cp'
                continue

            statut_matched = False
            for statut in STATUTS:
                if line.startswith(statut):
                    current['journal_ou_statut'] = statut
                    phones = PHONE_RE.findall(line[len(statut):])
                    if len(phones) >= 1:
                        current['tel_bureau'] = phones[0]
                    if len(phones) >= 2:
                        current['tel_prive'] = phones[1]
                    phase = 'got_journal'
                    statut_matched = True
                    break
            if statut_matched:
                continue

            em = EMAIL_RE.search(line)
            if em and phase in ('got_journal', 'got_cp'):
                current['email'] = em.group()
                continue

            if phase == 'got_cp':
                cleaned = CARTE_INLINE_RE.sub('', line).strip()
                phones = PHONE_RE.findall(cleaned)
                journal = cleaned
                for p in phones:
                    journal = journal.replace(p, '').strip()
                journal = clean_ocr_icons(journal).strip(' ,')
                current['journal_ou_statut'] = journal
                if len(phones) >= 1:
                    current['tel_bureau'] = phones[0]
                if len(phones) >= 2:
                    current['tel_prive'] = phones[1]
                phase = 'got_journal'
                continue

            if phase in ('got_name', 'got_addr'):
                if not current['adresse']:
                    current['adresse'] = line.rstrip(',')
                else:
                    current['adresse'] += ', ' + line.rstrip(',')
                phase = 'got_addr'

        if current and current['nom']:
            fiches.append(current)
        return fiches
