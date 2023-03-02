
class Ville:
    def __init__(self, nom, population):
        self.nom = nom
        self.population = population

    def get_nom(self):
        return self.nom
    
    def get_population(self):
        return self.population

    def set_population(self, population):
        self.population = population
    
class Personne:
    def __init__(self, nom, age, ville):
        self.nom = nom
        self.age = age
        self.ville = ville
        
    def get_nom(self):
        return self.nom
    
    def get_age(self):
        return self.age
    
    def get_ville(self):
        return self.ville
    
    def set_ville(self, ville):
        self.ville = ville

    def ajouterPopulation(self):
        self.ville.set_population(self.ville.get_population() + 1)

ville1 = Ville("Paris", 1000000)
ville2 = Ville("Marseille", 861635)

print("Population de la ville de Paris :", ville1.get_population(), "habitants.")
print("Population de la ville de Marseille :", ville2.get_population(), "habitants.")

myrtille = Personne("Myrtille", 4, ville1)
jean = Personne("Jean", 25, ville1)
chloe = Personne("Chloe", 18, ville2)

myrtille.ajouterPopulation()
jean.ajouterPopulation()
chloe.ajouterPopulation()

print("Mise à jour de la ville de Paris :", ville1.get_population(), "habitants.")
print("Mise à jour de la ville de Marseille :", ville2.get_population(), "habitants.")