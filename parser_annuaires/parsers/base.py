"""
Classe de base pour tous les parseurs de format d'annuaire.

Pour ajouter un nouveau format (ex: Format D pour les annuaires 1895-1930) :
  1. Créer parser_annuaires/parsers/format_d.py avec class FormatDParser(BaseParser)
  2. Implémenter detect_page() et parse()
  3. Surcharger extract_lines() si le layout est différent (ex: 3 colonnes)
  4. Enregistrer le parseur dans parsers/__init__.py
"""
from abc import ABC, abstractmethod


class BaseParser(ABC):
    """Interface commune à tous les parseurs d'annuaire de presse belge."""

    format_id: str   # Identifiant court, ex: 'a', 'b', 'c', 'd'
    description: str # Ex: "1995-1999 — 2 colonnes, carte inline"
    is_default: bool = False  # True pour le format de repli (un seul par registry)

    @abstractmethod
    def detect_page(self, page_text: str) -> bool:
        """Retourne True si le contenu de cette page correspond au format.

        Appelé lors de la détection automatique. Les parseurs non-default
        doivent implémenter une détection positive ; le parseur default
        sert de repli et peut retourner False ici.
        """
        ...

    def extract_lines(self, page) -> list[str]:
        """Extrait les lignes de texte depuis une page pdfplumber.

        Par défaut : extraction 2 colonnes avec détection automatique de gouttière.
        Surcharger pour les layouts différents (1 colonne, 3 colonnes, etc.).
        """
        from ..extraction import extract_two_columns
        return extract_two_columns(page)

    @abstractmethod
    def parse(self, lines: list[str], debug: bool = False) -> list[dict]:
        """Parse les lignes extraites et retourne une liste de fiches.

        Chaque fiche est un dict produit par models.new_fiche().
        """
        ...
