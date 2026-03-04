"""
Pipeline principal : chargement PDF → détection → extraction → parsing.
"""
from pathlib import Path
from .parsers import REGISTRY
from .detection import detect_format


def process_pdf(
    pdf_path,
    fmt: str | None = None,
    page_ranges: list[tuple[int, int]] | None = None,
    label: str | None = None,
    debug: bool = False,
) -> list[dict]:
    """Parse un fichier PDF d'annuaire et retourne la liste des fiches.

    Args:
        pdf_path:    Chemin vers le PDF (str ou Path).
        fmt:         Format forcé ('a', 'b', 'c', ...). Si None, auto-détection.
        page_ranges: Plages de pages [(début, fin), ...]. Si None, tout le PDF.
        label:       Étiquette d'annuaire (défaut : nom du fichier sans extension).
        debug:       Affiche les lignes parsées ligne par ligne.

    Returns:
        Liste de fiches (dict) avec champs standards + 'annuaire' + 'page'.
    """
    import pdfplumber

    pdf_path = Path(pdf_path)
    label = label or pdf_path.stem
    all_fiches = []

    with pdfplumber.open(pdf_path) as pdf:
        total = len(pdf.pages)
        page_set = None

        if page_ranges:
            page_set = set()
            for start, end in page_ranges:
                for p in range(max(1, start), min(total, end) + 1):
                    page_set.add(p)
            pages_iter = [(p, pdf.pages[p - 1]) for p in sorted(page_set)]
            desc = ','.join(f'{s}-{e}' for s, e in page_ranges)
            print(f"[{pdf_path.name}] Pages {desc} ({len(pages_iter)} pages)")
        else:
            pages_iter = [(p + 1, page) for p, page in enumerate(pdf.pages)]
            print(f"[{pdf_path.name}] Toutes les pages ({total})")

        if fmt is None:
            fmt = detect_format(pdf, page_set=page_set)
            print(f"  Format détecté : {fmt.upper()}")

        if fmt not in REGISTRY:
            raise ValueError(f"Format inconnu : '{fmt}'. Formats disponibles : {list(REGISTRY)}")

        parser = REGISTRY[fmt]

        for page_num, page in pages_iter:
            try:
                lines  = parser.extract_lines(page)
                fiches = parser.parse(lines, debug=debug)
            except Exception as e:
                print(f"  p.{page_num:>4d} ⚠ ERREUR: {e}")
                continue
            if fiches:
                for f in fiches:
                    f['annuaire'] = label
                    f['page']     = page_num
                all_fiches.extend(fiches)
                if not debug:
                    print(f"  p.{page_num:>4d} → {len(fiches):>3d} fiches")

    n = len(all_fiches)
    if n:
        no_carte = sum(1 for f in all_fiches if not f.get('carte_presse'))
        no_cp    = sum(1 for f in all_fiches if not f.get('code_postal'))
        no_jour  = sum(1 for f in all_fiches if not f.get('journal_ou_statut'))
        no_nom   = sum(1 for f in all_fiches if not f.get('nom'))
        print(f"  TOTAL : {n} fiches")
        if no_nom or no_carte or no_cp or no_jour:
            print(f"  ⚠ Qualité : {no_nom} sans nom, {no_carte} sans carte, "
                  f"{no_cp} sans CP, {no_jour} sans journal")
    else:
        print("  TOTAL : 0 fiches")
    print()
    return all_fiches
