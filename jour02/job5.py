class Voiture:
    def __init__(self, marque, modele, annee, kilometrage):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.kilometrage = kilometrage
        self.en_marche = False
        self.reservoir = 50
    
    def get_marque(self):
        return self.marque
    
    def set_marque(self, marque):
        self.marque = marque
    
    def get_modele(self):
        return self.modele
    
    def set_modele(self, modele):
        self.modele = modele
    
    def get_annee(self):
        return self.annee
    
    def set_annee(self, annee):
        self.annee = annee
    
    def get_kilometrage(self):
        return self.kilometrage
    
    def set_kilometrage(self, kilometrage):
        self.kilometrage = kilometrage
    
    def get_en_marche(self):
        return self.en_marche
    
    def demarrer(self):
        if self.verifier_plein() > 5:
            self.en_marche = True
        else:
            print("Le réservoir est presque vide, la voiture ne peut pas démarrer.")
    
    def arreter(self):
        self.en_marche = False
    
    def verifier_plein(self):
        return self.reservoir
    
ma_voiture = Voiture("Peugeot", "207", 2021, 10000)
ma_voiture.set_marque("Renault")
print(ma_voiture.get_marque())

ma_voiture.demarrer()
ma_voiture.reservoir = 10
ma_voiture.demarrer()

print(ma_voiture.get_en_marche())

ma_voiture.arreter()
print(ma_voiture.get_en_marche())