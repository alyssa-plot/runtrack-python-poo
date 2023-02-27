class Point:

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def afficherlespoints(self):
        print(self.x,self.y)

afficheXY = Point(3,3)
afficheXY.afficherlespoints()

changeXY = Point(7,7)
changeXY.afficherlespoints()