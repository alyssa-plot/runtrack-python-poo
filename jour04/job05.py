class Forme:
    def aire(self):
        return 0
    
class Rectangle(Forme):

    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur

    def aire(self):
        return self.largeur*self.hauteur
    
class Cercle(Forme):

    def __init__(self, radius):
        self.radius = radius

    def aire(self):
        return 3.14*self.radius**2

rectangle1 = Rectangle(6,3)
print("L'aire du rectangle est de", rectangle1.aire())

cercle1 = Cercle(5)
print("L'aire du cercle est de", cercle1.aire())