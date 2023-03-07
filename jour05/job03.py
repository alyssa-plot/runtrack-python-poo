def longueur(chaine):
    if chaine == "":
        return 0
    else:
        return 1 + longueur(chaine[1:])

chaine = input("Entrez un caractère: ")

resultat = longueur(chaine)
print(f"La longueur de la chaîne '{chaine}' est {resultat}")