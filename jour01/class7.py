class Personnage:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def droite(self):
        self.x += 1

    def gauche(self):
        self.x -= 1
    
    def haut(self):
        self.y -= 1
    
    def bas(self):
        self.y += 1
    
    def position(self):
        return (self.x, self.y)
    
position1 = Personnage(3,3)
print(position1.position())
position1.gauche()
position1.bas()