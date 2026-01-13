a = 2 
print("coucou", a)


def moyenne(liste):
    """Retourne la moyenne des valeurs d'une liste."""
    if not liste:
        return 0
    return sum(liste) / len(liste)