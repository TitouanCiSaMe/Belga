#!/usr/bin/env python3
"""
Point d'entrée de compatibilité — délègue au package parser_annuaires.

Usage (inchangé) :
    python parser_annuaires_v2.py annuaire_2003.pdf -o fiches.xlsx
    python parser_annuaires_v2.py annuaire_2000.pdf --format b --pages 155-390 -o fiches.xlsx
"""
from parser_annuaires.cli import main

if __name__ == '__main__':
    main()
