"""
Interface en ligne de commande du parser d'annuaires de presse belge.
"""
import argparse
import logging
import sys
from pathlib import Path

from .parsers import REGISTRY
from .pipeline import process_pdf
from .export import fiches_to_excel


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Parser unifié — Annuaires de la Presse Belge (1895-2024)"
    )
    parser.add_argument('pdfs', nargs='+', help="Fichier(s) PDF à parser")
    parser.add_argument(
        '--format', '-f',
        choices=list(REGISTRY.keys()),
        default=None,
        help="Format forcé (défaut : auto-détection)"
    )
    parser.add_argument(
        '--pages', type=str, default=None,
        help="Plage(s) de pages, ex: 155-390 ou 155-390,560-800"
    )
    parser.add_argument('--label', type=str, default=None,
                        help="Étiquette personnalisée pour l'annuaire")
    parser.add_argument('--output', '-o', type=str, default='annuaire_fiches.xlsx',
                        help="Fichier Excel de sortie (défaut: annuaire_fiches.xlsx)")
    parser.add_argument('--dico', type=str, default=None,
                        help="Dictionnaire médias JSON pour normalisation post-parsing")
    parser.add_argument('--debug', action='store_true',
                        help="Affiche le parsing ligne par ligne")
    parser.add_argument('--dry-run', action='store_true',
                        help="Analyse sans écrire de fichier Excel")
    args = parser.parse_args()

    logging.basicConfig(
        level=logging.DEBUG if args.debug else logging.INFO,
        format='%(levelname)s: %(message)s'
    )

    if args.dico and not Path(args.dico).exists():
        print(f"ERREUR: Dictionnaire introuvable : {args.dico}")
        sys.exit(1)

    page_ranges = None
    if args.pages:
        page_ranges = []
        for part in args.pages.split(','):
            se = part.strip().split('-')
            if len(se) == 2:
                page_ranges.append((int(se[0]), int(se[1])))
            else:
                print(f"Format de plage invalide : {part}")
                sys.exit(1)

    all_fiches = []
    for pdf_path in args.pdfs:
        fiches = process_pdf(
            pdf_path,
            fmt=args.format,
            page_ranges=page_ranges,
            label=args.label,
            debug=args.debug,
        )
        all_fiches.extend(fiches)

    if all_fiches and args.dico:
        from nettoyeur import nettoyer_fiches
        all_fiches = nettoyer_fiches(all_fiches, args.dico)

    if args.dry_run:
        print(f"[dry-run] {len(all_fiches)} fiches extraites, pas d'export.")
    elif all_fiches:
        fiches_to_excel(all_fiches, args.output)
    else:
        print("Aucune fiche trouvée !")


if __name__ == '__main__':
    main()
