class Cercle:
    def __init__(self,rayon):
        self.rayon = rayon
        self.cironference = self.rayon * 3,14
        self.aire = self.rayon * self.rayon * 3.14
        self.diametre = self.rayon * 2

    def changer_rayon(self):
        pass

    def afficher_info(self):
        print("Le rayon est de : ",self.rayon, f'\n',"La cironférence est de : ",self.cironference,f'\n',"L'aire du carré est de : ",self.aire,f'\n',"le diamètre est de : ", self.diametre)

    def circonference(self):
        return(self.cironference)

    def aire(self):
        return(self.aire)

    def diametre(self):
        return(self.diametre)

cercle1 = Cercle(2)
cercle1.afficher_info()
cercle2 = Cercle(8)
cercle2.afficher_info()