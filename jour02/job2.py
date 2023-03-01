class Livre:
    def __init__(self):
        self.titre = ""
        self.auteur = ""
        self.pages = ""
    
    def set_titre(self, titre):
        self.titre = titre

    def get_titre(self):
        return self.titre
    
    def set_auteur(self, auteur):
        self.auteur = auteur
    
    def get_auteur(self):
        return self.auteur
    
    def set_pages(self, pages):
        if isinstance(pages, int) and pages >= 0:
            self.pages = pages
        else:
            print("erreur : le nombre de pages doit être un nombre entier positif")

    def get_pages(self):
        return self.pages
    

livre1 = Livre()
livre1.set_titre("L'immoraliste")
livre1.set_auteur("André Gide")
livre1.set_pages(100)
print(livre1.get_titre())
print(livre1.get_auteur())
print(livre1.get_pages())
livre1.set_pages(-10)
livre1.set_pages(10)
print(livre1.get_pages())