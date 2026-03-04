"""
parser_annuaires — Extraction structurée des Annuaires de la Presse Belge (1895-2024).

Structure du package :
    constants.py   — Regex et constantes partagées
    models.py      — Structure de données (fiche journaliste)
    text_utils.py  — Nettoyage OCR et normalisation textuelle
    extraction.py  — Extraction des lignes depuis les pages PDF
    detection.py   — Détection automatique du format
    pipeline.py    — Pipeline principal (PDF → fiches)
    export.py      — Export Excel (.xlsx)
    cli.py         — Interface ligne de commande
    parsers/       — Un module par format de layout
        base.py        Interface BaseParser
        format_a.py    1995-1999 (2 col., carte inline)
        format_b.py    2000-2002 (2 col., contacts labellisés)
        format_c.py    2003+     (1 col., séparation par puces)

Pour ajouter un nouveau format (ex: annuaires 1895-1930) :
    1. Créer parsers/format_d.py avec class FormatDParser(BaseParser)
    2. L'enregistrer dans parsers/__init__.py : REGISTRY['d'] = FormatDParser()
"""
from .pipeline import process_pdf
from .parsers import REGISTRY

def fiches_to_excel(fiches, output_path):
    """Proxy vers export.fiches_to_excel (import différé pour éviter openpyxl au chargement)."""
    from .export import fiches_to_excel as _fn
    return _fn(fiches, output_path)

__all__ = ['process_pdf', 'fiches_to_excel', 'REGISTRY']
