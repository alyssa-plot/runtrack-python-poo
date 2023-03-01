class Livre:
    def __init__(self, titre, auteur, pages):
        self.titre = ""
        self.auteur = ""
        self.pages = ""
        self.__disponible = True
    
    def set_titre(self, titre):
        self.titre = titre

    def get_titre(self):
        return self.titre
    
    def set_auteur(self, auteur):
        self.auteur = auteur
    
    def get_auteur(self):
        return self.auteur
    
    def verification(self):
        return self.__disponible
    
    def emprunter(self):
        if self.verification():
            self.__disponible = False
            print("Le livre", self.titre, "a été emprunté.")
        else:
            print("Le livre", self.titre, "n'est pas disponible.")
    
    def rendre(self):
        if not self.verification():
            self.__disponible = True
            print("Le livre", self.titre, "a été rendu.")
        else:
            print("Le livre", self.titre, "n'a pas été emprunté.")
    
    def get_titre(self):
        return self.titre
    
    def get_auteur(self):
        return self.auteur
    
    def get_pages(self):
        return self.pages
    
livre1 = Livre("L'immoraliste", "André Gide", 500)

# Vérification de la disponibilité
if livre1.verification():
    print("Le livre", livre1.get_titre(), "est disponible.")
else:
    print("Le livre", livre1.get_titre(), "n'est pas disponible.")

# Emprunt du livre
livre1.emprunter()

# Vérification de la disponibilité
if livre1.verification():
    print("Le livre", livre1.get_titre(), "est disponible.")
else:
    print("Le livre", livre1.get_titre(), "n'est pas disponible.")

# Rendu du livre
livre1.rendre()

# Vérification de la disponibilité
if livre1.verification():
    print("Le livre", livre1.get_titre(), "est disponible.")
else:
    print("Le livre", livre1.get_titre(), "n'est pas disponible.")