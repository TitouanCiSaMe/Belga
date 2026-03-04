"""
Structure de données commune : la fiche journaliste.
"""


def new_fiche(**kw) -> dict:
    """Crée une fiche vide avec tous les champs standards."""
    f = {
        'nom': '', 'prenom': '', 'carte_presse': '', 'specialisation': '',
        'adresse': '', 'code_postal': '', 'ville': '',
        'journal_ou_statut': '',
        'tel_bureau': '', 'tel_prive': '', 'fax': '', 'gsm': '', 'email': '',
    }
    f.update(kw)
    return f
