"""
Extraction du texte brut depuis les pages PDF.

Gère les layouts à 1 colonne (format C) et 2 colonnes (formats A/B)
via une détection automatique de la gouttière centrale.
"""
from collections import Counter


def words_to_lines(words: list, y_tol: int = 5) -> list[str]:
    """Regroupe les mots PDF par ligne selon leur proximité verticale."""
    if not words:
        return []
    lines, cur = [], [words[0]]
    for w in words[1:]:
        if abs(w['top'] - cur[-1]['top']) <= y_tol:
            cur.append(w)
        else:
            cur.sort(key=lambda x: x['x0'])
            lines.append(' '.join(x['text'] for x in cur))
            cur = [w]
    cur.sort(key=lambda x: x['x0'])
    lines.append(' '.join(x['text'] for x in cur))
    return lines


def find_gutter(words: list, page_width: float) -> float:
    """Détecte la position x de la gouttière entre 2 colonnes.

    Utilise une analyse d'histogramme des positions de début de mot
    pour trouver le plus grand espace vide dans la zone centrale (25-75 %).
    Retourne le centre de cet espace, ou page_width/2 si rien n'est trouvé.
    """
    real = [w for w in words if len(w['text'].strip()) > 2]
    if not real:
        return page_width / 2
    step = 5
    buckets: Counter = Counter()
    for w in real:
        buckets[int(w['x0'] / step) * step] += 1
    min_b = (int(page_width * 0.25) // step) * step
    max_b = (int(page_width * 0.75) // step) * step
    best_start, best_end, best_size = None, None, 0
    gap_start = None
    for b in range(min_b, max_b + step, step):
        if buckets.get(b, 0) == 0:
            if gap_start is None:
                gap_start = b
        else:
            if gap_start is not None:
                size = b - gap_start
                if size > best_size:
                    best_size, best_start, best_end = size, gap_start, b
                gap_start = None
    if best_start is not None and best_size > 15:
        return (best_start + best_end) / 2
    return page_width / 2


def extract_two_columns(page) -> list[str]:
    """Extrait le texte d'une page à 2 colonnes (lecture gauche puis droite).

    La gouttière est détectée automatiquement via find_gutter.
    """
    words = page.extract_words(keep_blank_chars=True, x_tolerance=3, y_tolerance=3)
    if not words:
        return []
    mid_x = find_gutter(words, page.width)
    left  = sorted([w for w in words if w['x0'] < mid_x],  key=lambda w: (w['top'], w['x0']))
    right = sorted([w for w in words if w['x0'] >= mid_x], key=lambda w: (w['top'], w['x0']))
    return words_to_lines(left) + words_to_lines(right)


def extract_single_column(page) -> list[str]:
    """Extrait le texte d'une page à 1 colonne (format C et suivants)."""
    text = page.extract_text(x_tolerance=3, y_tolerance=3)
    if not text:
        return []
    return [line.strip() for line in text.split('\n') if line.strip()]
