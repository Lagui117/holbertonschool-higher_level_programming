#!/usr/bin/python3

class InvalidInputError(Exception):
    """Exception levée quand une entrée n'est pas valide."""
    pass


def add_positive_numbers(a, b):
    """Ajoute deux nombres positifs. 
    Lève InvalidInputError si un argument est invalide.
    """
    # Vérification des types
    if not isinstance(a, (int, float)):
        raise InvalidInputError("a doit être un nombre")
    if not isinstance(b, (int, float)):
        raise InvalidInputError("b doit être un nombre")

    # Vérification des valeurs
    if a < 0 or b < 0:
        raise InvalidInputError("les deux nombres doivent être positifs")

    return a + b