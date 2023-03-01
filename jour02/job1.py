class Rectangle:
    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur
    
    def longueur2(self):
        return self.longueur
    def longueur3(self, longueur):
        self.longueur = longueur

    def largeur2(self):
        return self.largeur
    def largeur3(self, largeur):
        self.largeur = largeur

rectangle = Rectangle(10, 5)
print("La longueur est : ", rectangle.longueur2())
print("La largeur est : ", rectangle.largeur2())

rectangle.longueur3(7)
rectangle.largeur3(7)
print("La longueur est : ", rectangle.longueur2())
print("La largeur est : ", rectangle.largeur2())