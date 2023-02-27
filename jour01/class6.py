class Animal:
    def __init__(self):
        self.age = 0
        self.prenom = ""

    def vieillir(self):
        self.age += 1
    
    def nommer(self):
        self.prenom = "Luna"

animal1 = Animal()
print("L'age de l'animal {}an".format(animal1.age))
animal1.nommer()
print("L'animal se nomme {}".format(animal1.prenom))

#activer pour le vieillir
#animal1.vieillir()
#print("L'age de l'animal {}an".format(animal1.age))
#print("L'animal se nomme {}".format(animal1.prenom))