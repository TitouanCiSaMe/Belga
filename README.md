# Parser — Annuaires de la Presse Belge (1895-2024)

Extraction structurée des fiches journalistes depuis les annuaires PDF de la presse belge.

## Installation

```bash
pip install pdfplumber openpyxl
```

## Utilisation rapide

```bash
# Auto-détection du format, export Excel
python -m parser_annuaires annuaire_2003.pdf -o fiches.xlsx

# Forcer un format, limiter les pages
python -m parser_annuaires annuaire_2000.pdf --format b --pages 155-390 -o fiches.xlsx

# Plusieurs PDFs en une passe
python -m parser_annuaires annuaire_2001.pdf annuaire_2002.pdf -o fiches_2001-2002.xlsx

# Vérifier sans écrire de fichier
python -m parser_annuaires annuaire_2003.pdf --dry-run

# Afficher le parsing ligne par ligne (diagnostic)
python -m parser_annuaires annuaire_2003.pdf --debug
```

## Options

| Option | Description |
|---|---|
| `--format {a,b,c,...}` | Forcer un format (défaut : auto-détection par vote) |
| `--pages X-Y[,A-B]` | Traiter uniquement ces plages de pages |
| `--label TEXTE` | Étiquette personnalisée pour la colonne "Annuaire" |
| `--output / -o FICHIER` | Chemin du fichier Excel (défaut : `annuaire_fiches.xlsx`) |
| `--dico FICHIER.json` | Dictionnaire médias JSON pour normalisation des journaux |
| `--dry-run` | Analyse sans écrire de fichier |
| `--debug` | Affichage détaillé du parsing page par page |

## Formats supportés

| ID | Période | Layout | Caractéristiques |
|---|---|---|---|
| `a` | 1995-1999 | 2 colonnes | Carte de presse sur la ligne du nom, contacts inline |
| `b` | 2000-2002 | 2 colonnes | Carte séparée, contacts labellisés (`Tél. bu.`, `GSM`…) |
| `c` | 2003+ | 1 colonne | Séparation par puces `•`, artefacts OCR importants |

La détection automatique échantillonne 5 pages et vote pour le format majoritaire.
En cas de doute, utiliser `--format` pour forcer.

## Colonnes du fichier Excel produit

`Nom` · `Prénom` · `N° Carte` · `Spécialisation` · `Adresse` · `Code Postal` · `Ville` · `Journal / Statut` · `Tél. Bureau` · `Tél. Privé` · `Fax` · `GSM` · `Email` · `Annuaire` · `Page`

## Utilisation comme bibliothèque Python

```python
from parser_annuaires import process_pdf, fiches_to_excel

fiches = process_pdf("annuaire_2003.pdf")
fiches_to_excel(fiches, "sortie.xlsx")
```

```python
# Accès au registre des parseurs
from parser_annuaires import REGISTRY
for fmt_id, parser in REGISTRY.items():
    print(fmt_id, parser.description)
```

## Ajouter un nouveau format

Pour les annuaires antérieurs à 1995 (layouts différents) :

**1. Créer `parser_annuaires/parsers/format_d.py`**

```python
from .base import BaseParser

class FormatDParser(BaseParser):
    format_id   = 'd'
    description = "1895-1930 — description du layout"

    def detect_page(self, page_text: str) -> bool:
        # Retourner True si ce texte de page correspond au format
        return "mot_clé_caractéristique" in page_text

    def extract_lines(self, page) -> list[str]:
        # Optionnel : surcharger si le layout est différent (ex: 3 colonnes)
        # Par défaut : extraction 2 colonnes avec détection de gouttière
        from ..extraction import extract_two_columns
        return extract_two_columns(page)

    def parse(self, lines: list[str], debug: bool = False) -> list[dict]:
        from ..models import new_fiche
        fiches = []
        # ... logique de parsing spécifique au format ...
        return fiches
```

**2. Enregistrer dans `parser_annuaires/parsers/__init__.py`**

```python
from .format_d import FormatDParser

REGISTRY: dict[str, BaseParser] = {
    'd': FormatDParser(),   # ← ajouter avant le format de repli 'a'
    'c': FormatCParser(),
    'b': FormatBParser(),
    'a': FormatAParser(),   # repli (is_default=True), toujours en dernier
}
```

Le nouveau format est immédiatement disponible via `--format d` et participera à l'auto-détection.

## Structure du projet

```
parser_annuaires/
├── constants.py     Regex et constantes partagées (artefacts OCR, statuts…)
├── models.py        Structure de données : new_fiche()
├── text_utils.py    Nettoyage OCR, normalisation des noms et cartes
├── extraction.py    Extraction PDF (1/2 colonnes, détection de gouttière)
├── detection.py     Auto-détection du format par vote
├── pipeline.py      Orchestration : PDF → fiches
├── export.py        Export Excel formaté
├── cli.py           Interface ligne de commande
└── parsers/
    ├── base.py      Classe abstraite BaseParser
    ├── __init__.py  Registre REGISTRY
    ├── format_a.py  Format A (1995-1999)
    ├── format_b.py  Format B (2000-2002)
    └── format_c.py  Format C (2003+)
```
