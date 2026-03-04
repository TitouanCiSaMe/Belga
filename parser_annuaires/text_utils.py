"""
Utilitaires de nettoyage et normalisation du texte OCR.
"""
import re
from .constants import OCR_ICON_TRAIL_RE, OCR_SUFFIX_RE, OCR_PREFIX_RE, PARTICLES


def clean_ocr_icons(text: str) -> str:
    """Supprime les artefacts OCR d'icônes en début/fin de ligne."""
    text = OCR_SUFFIX_RE.sub('', text)
    text = OCR_ICON_TRAIL_RE.sub('', text)
    text = OCR_PREFIX_RE.sub('', text)
    return text.strip()


def fix_spacing(text: str) -> str:
    """Corrige les espaces manquants : MERCKXAnnick → MERCKX Annick."""
    text = re.sub(r'([A-ZÉÈÊËÀÂÙÛÜÔÏÎ])([A-Z][a-zéèêëàâùûüôïî])', r'\1 \2', text)
    text = re.sub(r'([a-zéèêëàâùûüôïî,])([A-ZÉÈÊËÀÂÙÛÜÔÏÎ])', r'\1 \2', text)
    text = re.sub(r'(\d)([A-ZÉÈÊËÀÂ])', r'\1 \2', text)
    text = re.sub(r'([a-zéèêëàâùûüôïî])(\d)', r'\1 \2', text)
    return text


def split_nom_prenom(name_str: str) -> tuple[str, str]:
    """Sépare 'VAN DEN EYNDE Wim' en ('VAN DEN EYNDE', 'Wim').

    Gère les particules nobilaires FR/NL (de, van, ter, du, le...).
    """
    words = name_str.split()
    nom, prenom, found = [], [], False
    for w in words:
        stripped = re.sub(r'[^A-Za-zÉÈÊËÀÂÙÛÜÔÏÎéèêëàâùûüôïî\-\'\(\)]', '', w)
        if not stripped:
            continue
        if not found:
            w_core = stripped.replace("'", "").replace("-", "")
            is_upper    = w_core.isupper() and len(w_core) >= 1
            is_particle = stripped.lower() in PARTICLES
            if is_upper or is_particle:
                nom.append(w)
            else:
                found = True
                prenom.append(w)
        else:
            prenom.append(w)
    return ' '.join(nom), ' '.join(prenom)


def clean_carte(raw: str) -> str:
    """Normalise un numéro de carte de presse.

    'F438 S' → 'F4385', 'F28 S3' → 'F2853'  (S = artefact OCR du chiffre 5)
    """
    cleaned = re.sub(r'\s+S$', '5', raw)
    cleaned = re.sub(r'\s+S(\d)', r'5\1', cleaned)
    return cleaned.replace(' ', '')


def clean_prenom(prenom: str) -> str:
    """Supprime les artefacts OCR résiduels en fin de prénom."""
    prenom = re.sub(r'\s+(?:\d|Ük|<\*©•|fe|[/\\^<>©®•✎🌐]+[\?]?)$', '', prenom)
    return prenom.strip()
