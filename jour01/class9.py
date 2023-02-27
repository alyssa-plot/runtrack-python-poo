class Produit:
    def __init__(self, nom, prixHT, TVA):
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = TVA

    def calculerprixTTC(self):
        return self.prixHT * (1 + self.TVA/100)

    def afficher(self):
        print(f"Nom : {self.nom}")
        print(f"Prix HT : {self.prixHT}€")
        print(f"TVA : {self.TVA}%")
        print(f"Prix TTC : {self.calculerprixTTC()}€")

    def modifiernom(self, nouveaunom):
        self.nom = nouveaunom

    def modifierprixHT(self, nouveauprixHT):
        self.prixHT = nouveauprixHT

    def obtenirnom(self):
        return self.nom

    def obtenirprixHT(self):
        return self.prixHT

    def obtenirTVA(self):
        return self.TVA

produit1 = Produit("Bacon Vegan", 2.99, 20)
produit1.afficher()
produit2 = Produit("Cuisse de poulet", 5.59, 10)
produit2.afficher()

produit1.modifiernom("Bacon")
produit1.modifierprixHT(3.10)
nouveaunom = produit1.obtenirnom()
print(f"Le nouveau nom du produit 1 est {nouveaunom}.")
nouveauprixHT = produit1.obtenirprixHT()
print(f"Le nouveau prix HT du produit 1 est {nouveauprixHT}€.")