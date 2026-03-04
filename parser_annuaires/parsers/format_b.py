"""
Parseur Format B — Annuaires 2000-2002.

Layout : 2 colonnes, carte sur ligne séparée, contacts labellisés
(Tél. bu., Tél. pr., Fax, GSM, Email).
Gère les noms multi-lignes (lookahead) et les noms full-uppercase.
"""
import re
from .base import BaseParser
from ..constants import (
    CARTE_RE_AB, CP_VILLE_RE, NAME_BLACKLIST_STARTS,
    VOIR_RE, SKIP_HEADERS, CONTACT_RES, PARTICLES,
    EMAIL_RE,
)
from ..text_utils import clean_ocr_icons, fix_spacing, split_nom_prenom, clean_prenom, clean_carte
from ..models import new_fiche


class FormatBParser(BaseParser):
    format_id   = 'b'
    description = "2000-2002 — 2 colonnes, carte séparée, contacts labellisés"

    def detect_page(self, page_text: str) -> bool:
        return bool(re.search(r'T[eé]l\.\s*(?:bu|pr)\.', page_text))

    def _is_name(self, line: str) -> bool:
        """Détecte une ligne-nom format B (NOM Prénom), avec heuristique renforcée."""
        cleaned = clean_ocr_icons(line)
        if not cleaned or len(cleaned) < 4:
            return False
        if NAME_BLACKLIST_STARTS.match(cleaned):
            return False
        if CARTE_RE_AB.match(cleaned) or CP_VILLE_RE.match(cleaned):
            return False
        for _, pat in CONTACT_RES:
            if pat.match(cleaned):
                return False
        if re.match(r'^\d{1,3}$', cleaned) or cleaned in SKIP_HEADERS:
            return False

        words = cleaned.split()
        if len(words) < 2:
            return False

        first_alpha = re.sub(r'[^A-Za-zÉÈÊËÀÂÙÛÜÔÏÎéèêëàâùûüôïî]', '', words[0])
        if not first_alpha or len(first_alpha) < 2 or not first_alpha[0].isupper():
            return False

        # Trouver la frontière nom/prénom
        nom_words = []
        prenom_start = -1
        for i, w in enumerate(words):
            w_alpha = re.sub(r'[^A-Za-zÉÈÊËÀÂÙÛÜÔÏÎéèêëàâùûüôïî\-\']', '', w)
            if not w_alpha:
                continue
            w_core = w_alpha.replace("'", "").replace("-", "")
            if w_core.isupper() or w_alpha.lower() in PARTICLES:
                nom_words.append(w)
            else:
                prenom_start = i
                break

        if not nom_words or prenom_start < 0:
            return False

        prenom_first = re.sub(r'[^A-Za-zÉÈÊËÀÂÙÛÜÔÏÎéèêëàâùûüôïî]', '', words[prenom_start])
        if not prenom_first or not prenom_first[0].isupper():
            return False

        # Le nom doit contenir au moins un mot uppercase non-particule
        has_real_nom = any(
            len(re.sub(r'[^A-Za-z]', '', nw)) >= 2
            and re.sub(r'[^A-Za-z]', '', nw).isupper()
            and nw.lower() not in PARTICLES
            for nw in nom_words
        )
        if not has_real_nom:
            return False

        # Rejeter si le dernier mot du nom se termine par un tiret (mot coupé OCR)
        if nom_words[-1].endswith('-'):
            return False

        return True

    def parse(self, lines: list[str], debug: bool = False) -> list[dict]:
        fiches, current, phase = [], None, 'waiting'

        # Pré-traitement + indexation pour lookahead
        line_list = []
        for raw_line in lines:
            line = clean_ocr_icons(fix_spacing(raw_line.strip()))
            if line:
                line_list.append(line)

        i = 0
        while i < len(line_list):
            line = line_list[i]

            if (not line or line in SKIP_HEADERS
                    or re.match(r'^\d{1,3}$', line)
                    or re.match(r'^[FNA]-\d+$', line)):
                i += 1
                continue

            if VOIR_RE.match(line):
                if debug:
                    print(f"  [SKIP renvoi] {line}")
                i += 1
                continue

            if debug:
                print(f"  [{phase:12s}] {line}")

            # Contacts labellisés
            contact_matched = False
            for field, pat in CONTACT_RES:
                m = pat.match(line)
                if m and current:
                    val = m.group(1).strip()
                    if val:
                        current[field] = val
                    phase = 'contacts'
                    contact_matched = True
                    break
            if contact_matched:
                i += 1
                continue

            # Email isolé
            if phase == 'contacts' and current and '@' in line and not current.get('email'):
                current['email'] = line.strip()
                i += 1
                continue

            # Journal (après CP) — vérifié AVANT la détection de nom
            # pour éviter que "RTL-TVi" soit pris pour un nom,
            # mais seulement si la ligne n'est pas elle-même un nom de journaliste
            if phase == 'got_cp' and current and not self._is_name(line):
                current['journal_ou_statut'] = clean_ocr_icons(line)
                phase = 'got_journal'
                i += 1
                continue

            # Ligne-nom
            if self._is_name(line):
                if current and current.get('nom'):
                    fiches.append(current)
                name_clean = clean_ocr_icons(line)
                nom, prenom = split_nom_prenom(name_clean)
                prenom = clean_prenom(prenom)
                current = new_fiche(nom=nom, prenom=prenom)
                phase = 'got_name'

                # Lookahead : noms multi-lignes (ex: "ARGUELLES GONZALEZ\nMarcelino\nF3374")
                if i + 1 < len(line_list):
                    next_line  = line_list[i + 1]
                    next_clean = clean_ocr_icons(next_line)
                    is_structural = (
                        CARTE_RE_AB.match(next_clean)
                        or CP_VILLE_RE.match(next_clean)
                        or any(p.match(next_clean) for _, p in CONTACT_RES)
                        or self._is_name(next_clean)
                        or VOIR_RE.match(next_clean)
                    )
                    if (not is_structural
                            and next_clean
                            and next_clean[0].isupper()
                            and not next_clean[0].isdigit()
                            and len(next_clean.split()) <= 3
                            and not re.search(r'\d{4}', next_clean)
                            and not NAME_BLACKLIST_STARTS.match(next_clean)
                            and i + 2 < len(line_list)
                            and CARTE_RE_AB.match(clean_ocr_icons(line_list[i + 2]))):
                        current['prenom'] = (prenom + ' ' + next_clean).strip() if prenom else clean_prenom(next_clean)
                        if debug:
                            print(f"  [MULTILINE  ] +prénom: {next_clean}")
                        i += 1

                i += 1
                continue

            # Nom full-uppercase sans prénom sur la même ligne
            line_clean = clean_ocr_icons(line)
            if (line_clean
                    and not NAME_BLACKLIST_STARTS.match(line_clean)
                    and not CARTE_RE_AB.match(line_clean)
                    and not CP_VILLE_RE.match(line_clean)
                    and len(line_clean) >= 3
                    and line_clean.replace(' ', '').replace('-', '').replace("'", '').isalpha()
                    and line_clean.upper() == line_clean
                    and i + 2 < len(line_list)):
                next1 = clean_ocr_icons(line_list[i + 1])
                next2 = clean_ocr_icons(line_list[i + 2])
                if (next1 and next1[0].isupper() and not next1.isupper()
                        and len(next1.split()) <= 3
                        and not NAME_BLACKLIST_STARTS.match(next1)
                        and CARTE_RE_AB.match(next2)):
                    if current and current.get('nom'):
                        fiches.append(current)
                    current = new_fiche(nom=line_clean, prenom=clean_prenom(next1))
                    phase = 'got_name'
                    if debug:
                        print(f"  [FULLCAPS   ] {line_clean} + {next1}")
                    i += 2
                    continue

            if not current:
                i += 1
                continue

            # Carte (ligne isolée)
            if CARTE_RE_AB.match(line) and phase == 'got_name':
                current['carte_presse'] = clean_carte(line)
                phase = 'got_carte'
                i += 1
                continue

            # CP + Ville (virgule OCR en tête tolérée; journal collé capturé)
            line_for_cp = line.lstrip(',').strip()
            m_cp = CP_VILLE_RE.match(line_for_cp)
            if m_cp and phase in ('got_carte', 'got_addr', 'got_name'):
                current['code_postal'] = m_cp.group(1)
                current['ville'] = m_cp.group(2).strip()
                rest = line_for_cp[m_cp.end():].strip().lstrip(',').strip()
                if rest and not self._is_name(rest) and not CARTE_RE_AB.match(rest):
                    current['journal_ou_statut'] = rest
                    phase = 'got_journal'
                else:
                    phase = 'got_cp'
                i += 1
                continue

            # Adresse (détection d'un CP+Ville embarqué sur la même ligne)
            # Ex : "Boulevard Louis Schmidt 78, fi 1040 BRUXELLES, Basler Zeitung"
            if phase in ('got_carte', 'got_addr', 'got_name'):
                m_inline_cp = re.search(
                    r'\b(\d{4,5})\s+([A-ZÉÈÊËÀÂÙÛÜÔÏÎ][A-ZÉÈÊËÀÂÙÛÜÔÏÎ\s\-\'/\.]*)(?:\s*,\s*(.+))?$',
                    line,
                )
                if m_inline_cp and m_inline_cp.start() > 0:
                    addr_part = line[:m_inline_cp.start()].rstrip(', \t')
                    if addr_part:
                        if not current['adresse']:
                            current['adresse'] = addr_part
                        else:
                            current['adresse'] += ', ' + addr_part
                    current['code_postal'] = m_inline_cp.group(1)
                    current['ville'] = m_inline_cp.group(2).strip()
                    journal_part = (m_inline_cp.group(3) or '').strip()
                    if journal_part and not self._is_name(journal_part):
                        current['journal_ou_statut'] = journal_part
                        phase = 'got_journal'
                    else:
                        phase = 'got_cp'
                else:
                    if not current['adresse']:
                        current['adresse'] = line
                    else:
                        current['adresse'] += ', ' + line
                    phase = 'got_addr'

            i += 1

        if current and current.get('nom'):
            fiches.append(current)
        return fiches
