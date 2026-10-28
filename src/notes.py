def moyenne(liste):
    if not liste:
        raise ValueError("liste vide")
    return sum(liste) / len(liste)


def mention(moyenne):
    if moyenne >= 16:
        return "Très bien"
    if moyenne >= 14:
        return "Bien"
    if moyenne >= 12:
        return "Assez bien"
    if moyenne >= 10:
        return "Passable"
    return "Ajourné"