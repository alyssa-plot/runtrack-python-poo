class Rectangle:
    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur

    def perimetre(self):
        return 2 * (self.longueur + self.largeur)
    
    def surface(self):
         return self.longueur*self.largeur
    
class Parallelepipede(Rectangle):

    def __init__(self, longueur, largeur, hauteur):
        Rectangle.__init__(self,longueur,largeur)
        self.hauteur = hauteur

    def volume(self):
        return self.longueur*self.largeur*self.hauteur
    
Rectangle1 = Rectangle(12, 10)
print("Le paramètre du rectangle est de", Rectangle1.perimetre())
print("La surface du rectangle est de", Rectangle1.surface())
Parallelepipede1 = Parallelepipede(5,8,6)
print("La surface de mon parallelepipede est de", Parallelepipede1.volume())
