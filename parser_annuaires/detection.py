"""
Détection automatique du format d'un annuaire PDF.

Principe : vote sur un échantillon de pages.
Chaque parseur non-default est testé dans l'ordre du registre ;
le premier à matcher pour une page remporte son vote.
Les pages sans match donnent leur vote au parseur default.
"""
from collections import Counter
from .parsers import REGISTRY


def detect_format(pdf, page_set: set | None = None) -> str:
    """Détecte le format dominant d'un PDF par vote sur pages échantillons.

    Args:
        pdf:      Objet pdfplumber ouvert.
        page_set: Ensemble de numéros de pages (1-indexed) à considérer.
                  Si None, l'ensemble du document est échantillonné.

    Returns:
        Identifiant de format ('a', 'b', 'c', ...).
    """
    total = len(pdf.pages)

    if page_set:
        test_pages = sorted(page_set)[:min(7, len(page_set))]
    else:
        step = max(1, total // 5)
        test_pages = list(range(min(5, total - 1), total, step))[:5]
        if not test_pages:
            test_pages = [min(10, total - 1)]

    # Parseurs spécifiques (non-default) et identifiant du parseur de repli
    non_default = [(fid, p) for fid, p in REGISTRY.items() if not p.is_default]
    default_id  = next((fid for fid, p in REGISTRY.items() if p.is_default), 'a')

    votes: Counter = Counter()
    for p in test_pages:
        idx = (p - 1) if page_set else p
        if idx < 0 or idx >= total:
            continue
        page = pdf.pages[idx]
        text = page.extract_text(x_tolerance=3, y_tolerance=3) or ''

        matched = False
        for fmt_id, parser in non_default:
            if parser.detect_page(text):
                votes[fmt_id] += 1
                matched = True
                break
        if not matched:
            votes[default_id] += 1

    if not votes:
        return default_id

    winner = votes.most_common(1)[0][0]
    print(f"  Format votes: {dict(votes)} → {winner.upper()}")
    return winner
