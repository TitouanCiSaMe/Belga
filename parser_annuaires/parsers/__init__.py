"""
Registre des parseurs disponibles.

Pour ajouter un nouveau format :
  1. Créer parser_annuaires/parsers/format_X.py avec class FormatXParser(BaseParser)
  2. L'importer ici et l'ajouter à REGISTRY
  3. Les parseurs sont testés dans l'ordre d'insertion (priorité descendante).
     Le parseur default (is_default=True) doit être le dernier.
"""
from .base import BaseParser
from .format_c import FormatCParser
from .format_b import FormatBParser
from .format_a import FormatAParser

# Ordre : du plus spécifique au plus générique (le default 'a' est en dernier)
REGISTRY: dict[str, BaseParser] = {
    'c': FormatCParser(),
    'b': FormatBParser(),
    'a': FormatAParser(),
}

__all__ = ['BaseParser', 'REGISTRY']
