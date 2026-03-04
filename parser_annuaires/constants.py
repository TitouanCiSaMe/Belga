"""
Constantes et expressions régulières partagées par tous les parseurs.
"""
import re

PARTICLES = {'de', 'den', 'der', 'van', 'ten', 'ter', 'dit', 'dite',
             'el', 'da', 'di', 'du', 'le', 'la'}

CARTE_RE_AB     = re.compile(r'^[FNA][S/]?\d[\dS ]{2,5}$')
CARTE_RE_C      = re.compile(r'[FN]S?\d{4,5}')
CARTE_INLINE_RE = re.compile(r'[FN]S?\d{3,5}')

CP_VILLE_RE = re.compile(
    r'^(\d{4,5})\s+([A-ZÉÈÊËÀÂÙÛÜÔÏÎ][A-ZÉÈÊËÀÂÙÛÜÔÏÎ\s\-\'/\(\)\.]*)'
)

STATUTS = [
    'Pensionné actif', 'Pensionnéactif', 'Honoraire', 'Erelid',
    'Indépendant', 'Zelfstandige', 'Freelance',
    'Actief gepensioneerde', 'Aktief gepensioneerde',
]

SKIP_HEADERS = {'Redacteurs', 'Rédacteurs', 'Journalistes', 'Listes'}

VOIR_RE = re.compile(r'^Voir\s', re.I)

# Artefacts OCR
OCR_ICON_TRAIL_RE = re.compile(
    r'[\s]*(?:Ük|[/\\^<>*©®•✎🌐☎📞📠📧🖊🖋✒♂♀§†‡¶€£¥Üü])+\s*$'
)
OCR_SUFFIX_RE = re.compile(r'\s+(?:fe|Ük|<\*©•|[/\\^][\?]?)\s*$')
OCR_PREFIX_RE = re.compile(
    r'^(?:[/\\^✎🌐<>©®•][\s]*|fe\s+|Ük\s+|j\s+(?=[A-Z]))'
)

# Tags de spécialisation (format C)
SPEC_TAGS = {
    'ECO', 'POL', 'INT', 'REG', 'CULT', 'MED', 'SOC', 'SPO',
    'VFD', 'SCI', 'ENV', 'JUS', 'DEF',
}

# Contacts labellisés (format B)
TEL_BU_RE = re.compile(r'^Tél\.\s*bu\.\s*:?\s*(.*)')
TEL_PR_RE = re.compile(r'^Tél\.\s*pr\.\s*:?\s*(.*)')
FAX_RE    = re.compile(r'^Fax\s*:?\s*(.*)')
GSM_RE    = re.compile(r'^GSM\s*:?\s*(.*)')
EMAIL_PAT = re.compile(r'^Email\s*:?\s*(.*)', re.I)
CONTACT_RES = [
    ('tel_bureau', TEL_BU_RE), ('tel_prive', TEL_PR_RE),
    ('fax', FAX_RE), ('gsm', GSM_RE), ('email', EMAIL_PAT),
]

EMAIL_RE = re.compile(r'[\w\.\-]+@[\w\.\-]+')
PHONE_RE = re.compile(r'[\d/\.\-]{7,}')

NAME_BLACKLIST_STARTS = re.compile(
    r'^(?:Rue|Avenue|Av\.|Boulevard|Bd|Blvd|Chaussée|Chemin|Drève|Place|Impasse|'
    r'Route|Allée|Square|Quai|Clos|Sentier|Voie|Passage|'
    r'Straat|Laan|Weg|Plein|Steenweg|Dreef|Kaai|Lei|'
    r'Tél|Fax|GSM|Email|Tel\.|'
    r'Voir|See|Zie|'
    r'Pensionn|Honoraire|Erelid|Indépendant|Freelance|Zelfstandige|'
    r'Aktief|Actief|'
    r'l/l|CD|\+->|</l|ru\s|c$|i/l|S—|=3)\b',
    re.I
)
