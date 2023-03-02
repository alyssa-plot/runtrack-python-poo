class Personne:
    def __init__(self, age=14):
        self.age = age

    def afficher_age(self, age):
        self.age = age
        print("Cette personne est âgée de", self.age)

    def modifier_age(self, age1):
        self.age = age1
        print("C'est son anniversaire ! Désormais son âge est de", self.age)

    def bonjour(self):
        print("Hello")

class Eleve(Personne):
    def aller_en_cours(self):
        print("Je vais en cours")

    def affichage_age(self, age):
        self.age = age
        print("J'ai", self.age, "ans")

class Personne:
    def __init__(self, age=14):
        self.age = age

    def afficher_age(self, age):
        self.age = age
        print("Cette personne est âgée de", self.age)

    def modifier_age(self, age1):
        self.age = age1
        print("C'est son anniversaire ! Désormais son âge est de", self.age)

    def bonjour(self):
        print("Hello")

class Eleve(Personne):
    def aller_en_cours(self):
        print("Je vais en cours")

    def affichage_age(self, age):
        self.age = age
        print("J'ai", self.age, "ans")

class Professeur:
    def __init__(self, matièrenseignée):
        self.matièrenseignée = matièrenseignée
    
    def afficher_matière(self, matièrenseignée1):
        self.matièrenseignée = matièrenseignée1
        print("La matière de ce professeur est", self.matièrenseignée)
    
    def bonjour1(self):
        print("Bonjour, je suis votre professeur pour cette matière.")
    
    def enseigner(self):
        print("Le cours va commencer")

e1 = Eleve()
e1.bonjour()
e1.aller_en_cours()
e1.modifier_age(15)

pr1 = Professeur("Histoire")
pr1.bonjour1()
pr1.afficher_matière("histoire & géographie")
pr1.enseigner()


