"""
Parseur Format C — Annuaires 2003+.

Layout : 1 colonne, entrées séparées par des puces (•), artefacts OCR importants.
Le nom et la carte sont sur la même ligne ; les données suivantes sont segmentées.
"""
import re
from .base import BaseParser
from ..constants import (
    CARTE_RE_C, CP_VILLE_RE, NAME_BLACKLIST_STARTS,
    VOIR_RE, STATUTS, SPEC_TAGS, EMAIL_RE, PHONE_RE,
)
from ..text_utils import clean_ocr_icons, fix_spacing, split_nom_prenom, clean_prenom
from ..models import new_fiche
from ..extraction import extract_single_column

_EMAIL_PREFIX_STRIP = re.compile(r'^(?:El|K[lp]?|SI|DSl|O|#[=*»])(?:bu|pr)\s*', re.I)

_SKIP_PATTERNS = [re.compile(p) for p in [
    r'^Journalistes$', r'^Listes?$', r'^R[eé]dacteurs$',
    r'^1/1$', r'^CD$', r'^[+\-=ro1c]$', r'^ro\s', r'^[=\-]{2,}',
]]


class FormatCParser(BaseParser):
    format_id   = 'c'
    description = "2003+ — 1 colonne, séparation par puces, OCR intensif"

    def detect_page(self, page_text: str) -> bool:
        return page_text.count('•') > 3

    def extract_lines(self, page) -> list[str]:
        return extract_single_column(page)

    # ── Helpers privés ──────────────────────────────────────────

    def _clean_email(self, text: str) -> str | None:
        """Supprime les préfixes OCR corrompus des adresses email."""
        cleaned = _EMAIL_PREFIX_STRIP.sub('', text)
        m = EMAIL_RE.search(cleaned)
        return m.group() if m else None

    def _parse_name(self, line: str):
        """Retourne (nom, prenom, carte, spec) ou None."""
        m = CARTE_RE_C.search(line)
        if not m:
            return None
        carte = m.group()
        name_part = re.sub(r'\s*[~•]$', '', line[:m.start()]).strip()
        name_part = clean_ocr_icons(name_part)
        if not name_part or len(name_part.split()) < 2:
            return None
        first = re.sub(r'[^A-Za-zÉÈÊËÀÂÙÛÜÔÏÎéèêëàâùûüôïî\-\'\(\)]', '', name_part.split()[0])
        if not first or not first[0].isupper():
            return None
        if NAME_BLACKLIST_STARTS.match(name_part):
            return None
        nom, prenom = split_nom_prenom(name_part)
        prenom = clean_prenom(prenom)
        after = line[m.end():].strip()
        specs = [re.sub(r'[^A-Z]', '', t) for t in re.split(r'[\s/]+', after)]
        spec = '/'.join(s for s in specs if s in SPEC_TAGS)
        return nom, prenom, carte, spec

    def _parse_data_segments(self, raw_text: str) -> dict:
        """Segmente les données d'une entrée (séparées par •) en champs structurés."""
        result = new_fiche()
        text = raw_text

        # Protège les emails contre la segmentation par •
        placeholders = {}
        for idx, m in enumerate(EMAIL_RE.finditer(text)):
            ph = f'__EM{idx}__'
            placeholders[ph] = m.group()
        for ph, em in placeholders.items():
            text = text.replace(em, ph)
        text = fix_spacing(text)
        for ph, em in placeholders.items():
            text = text.replace(ph, em)

        segments = [s.strip() for s in text.split('•') if s.strip()]
        info_segs, tel_bu, tel_pr, fax_l, gsm_l, email_l = [], [], [], [], [], []

        for seg in segments:
            s = seg.strip()
            if not s:
                continue
            if re.match(r'^[©®]bu', s):
                tel_bu.extend(PHONE_RE.findall(s))
                continue
            if re.match(r'^[©®]pr', s):
                tel_pr.extend(PHONE_RE.findall(s))
                continue
            if re.match(r'^©gsm', s):
                gsm_l.extend(PHONE_RE.findall(s))
                continue
            if re.match(r'^[\^#<■\\]|^•p', s):
                em = self._clean_email(s)
                if em:
                    email_l.append(em)
                else:
                    fax_l.extend(PHONE_RE.findall(s))
                continue
            if re.match(r'^(?:El|K[lp]?|SI|DSl|O)(?:bu|pr)', s):
                em = self._clean_email(s)
                if em:
                    email_l.append(em)
                continue
            info_segs.append(s)

        for seg in info_segs:
            em_m = EMAIL_RE.search(seg)
            if em_m:
                email_l.append(em_m.group())
                seg = (seg[:em_m.start()] + seg[em_m.end():]).strip()
            m_cp = CP_VILLE_RE.search(seg)
            if m_cp and not result['code_postal']:
                before = seg[:m_cp.start()].strip().rstrip(',')
                if before and not result['adresse']:
                    result['adresse'] = before
                result['code_postal'] = m_cp.group(1)
                result['ville'] = m_cp.group(2).strip().rstrip('.')
                continue
            is_statut = False
            for st in STATUTS:
                if seg.startswith(st):
                    result['journal_ou_statut'] = st
                    tel_bu.extend(PHONE_RE.findall(seg[len(st):]))
                    is_statut = True
                    break
            if is_statut:
                continue
            has_num = bool(re.search(r'\d', seg))
            if not result['adresse'] and not result['code_postal'] and has_num:
                result['adresse'] = seg.rstrip(',').strip()
            elif not result['journal_ou_statut']:
                result['journal_ou_statut'] = seg.strip()
            elif not result['adresse'] and has_num:
                result['adresse'] = seg.rstrip(',').strip()

        if tel_bu:  result['tel_bureau'] = tel_bu[0]
        if tel_pr:  result['tel_prive']  = tel_pr[0]
        if fax_l:   result['fax']        = fax_l[0]
        if gsm_l:   result['gsm']        = gsm_l[0]
        if email_l: result['email']      = email_l[0]
        return result

    def _should_skip(self, line: str) -> bool:
        if re.match(r'^[FN]?-?\d{1,3}$', line):
            return True
        if len(line) <= 3 and not any(c.isalpha() for c in line):
            return True
        return any(p.match(line) for p in _SKIP_PATTERNS)

    # ── Interface BaseParser ─────────────────────────────────────

    def parse(self, lines: list[str], debug: bool = False) -> list[dict]:
        groups, cur_name, cur_data = [], None, []

        for line in lines:
            if self._should_skip(line):
                continue
            if VOIR_RE.match(line):
                continue
            parsed = self._parse_name(line)
            if parsed:
                if cur_name is not None:
                    groups.append((cur_name, cur_data))
                cur_name, cur_data = parsed, []
                if debug:
                    print(f"  >>> NOM: {parsed[0]} {parsed[1]} [{parsed[2]}] spec={parsed[3]}")
            else:
                cur_data.append(line)
                if debug:
                    print(f"      data: {line}")

        if cur_name is not None:
            groups.append((cur_name, cur_data))

        fiches = []
        for (nom, prenom, carte, spec), data_lines in groups:
            fields = self._parse_data_segments(' '.join(data_lines))
            fields['nom']           = nom
            fields['prenom']        = prenom
            fields['carte_presse']  = carte
            fields['specialisation'] = spec
            fiches.append(fields)
        return fiches
