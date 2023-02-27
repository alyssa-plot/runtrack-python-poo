class Personne:
    def __init__(self, prenom, nom):
        self.nom = nom
        self.prenom = prenom

    def resultat(self):
        print("Je suis" + self.prenom + self.nom)

Personne1 = Personne(" John ","Doe")
Personne1.resultat()
Personne2 = Personne(" Jean ","Dupond")
Personne2.resultat()