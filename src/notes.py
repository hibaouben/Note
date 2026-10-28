def moyenne(liste):
    if not liste:
        raise ValueError("liste vide")
    return sum(liste) / len(liste)