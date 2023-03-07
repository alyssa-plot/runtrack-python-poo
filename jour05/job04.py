liste = (1,2,8,3,7)
def nombre(liste):
    if len(liste) == 1:
        return liste[0]
    else:
        nombre2 = nombre(liste[1:])
        return liste[0] if liste[0] > nombre2 else nombre2

print(nombre(liste))