x = int(input("Entrez un nombre entier: "))
nombre = int(input("Entrez la puissance: "))

def puissance(x, nombre):
    if nombre == 0:
        return 1
    elif nombre % 2 == 0:
        y = puissance(x, nombre//2)
        return y*y
    else:
        y = puissance(x, (nombre-1)//2)
        return x*y*y

resultat = puissance(x, nombre)
print(f"{x}^{nombre} = {resultat}")