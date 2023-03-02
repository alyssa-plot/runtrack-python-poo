class CompteBancaire:
    def __init__(self, numero, nom, prenom, solde, decouvert=False):
        self.numero = numero
        self.nom = nom
        self.prenom = prenom
        self.solde = solde
        self.decouvert = decouvert
    
    def afficher(self):
        print(f"Numéro de compte : {self.numero}")
        print(f"Nom : {self.nom}")
        print(f"Prénom : {self.prenom}")
        print(f"Solde : {self.solde}")
    
    def afficherSolde(self):
        print(f"Solde : {self.solde}")
    
    def versement(self, montant):
        self.solde += montant
        print(f"Versement de {montant} effectué. Nouveau solde : {self.solde}")
    
    def retrait(self, montant):
        if self.solde - montant < 0 and not self.decouvert:
            print("Opération impossible : solde insuffisant.")
        else:
            self.solde -= montant
            print(f"Retrait de {montant} effectué. Nouveau solde : {self.solde}")
    
    def agios(self, taux):
        if self.solde < 0:
            agios = abs(self.solde) * taux
            self.solde -= agios
            print(f"Des agios de {agios} ont été appliqués. Nouveau solde : {self.solde}")
    
    def virement(self, compte_destinataire, montant):
        if self.solde - montant < 0 and not self.decouvert:
            print("Opération impossible : solde insuffisant.")
        else:
            self.solde -= montant
            compte_destinataire.solde += montant
            print("Virement effectué avec succès.")

compte1 = CompteBancaire("123456", "Dupont", "Jean", 1000)
compte1.afficher()
compte1.afficherSolde()
compte1.versement(500)
compte1.retrait(200)
compte1.agios(0.05)
compte2 = CompteBancaire("654321", "Martin", "Marie", -500, True)

compte1.virement(compte2, 700)