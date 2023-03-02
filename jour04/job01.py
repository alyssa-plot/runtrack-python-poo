#À l’aide du code python que je t'envoie et de la classe “Personne” , Eleve et Professeur écrite au-dessus, faites dire bonjour à votre élève grâce à la méthode “bonjour” ainsi que “je vais en cours” grâce à la méthode “allerEnCours”. Redéfinir l’age de l’élève à 15 ans. Créer un objet Professeur, 40 ans, faite dire bonjour à votre professeur et commencer le cours grâce à la méthode enseigner.

class Personne:
    def __init__(self, age=14):
        self.age = age

    def afficher_age(self, age):
        self.age = age
        print("Cette personne est agée de", self.age)

    def modifier_Age(self, age1):
        self.age = age1
        print("C'est son anniversaire ! Désormais son âge est de", self.age)
    
    def bonjour(self):
        print("Hello")

class Eleve(Personne):
    def allerEnCours(self):
        print("Je vais en cours")

    def affichageAge(self, age):
        self.age = age
        print("J'ai", self.age, "ans")

class Professeur:
    def __init__(self, matièrenseignée):
        self.matièrenseignée = matièrenseignée
    
    def afficher_matière(self, matièrenseignée1):
        self.matièrenseignée = matièrenseignée1
        print("La matière de ce professeur est", self.matièrenseignée)
    
    def enseigner(self):
        print("Le cours va commencer")

p1 = Personne()
p1.bonjour()
p1.afficher_age(14)
p1.modifier_Age(15)

e1 = Eleve()
e1.allerEnCours()
e1.affichageAge(15)

pr1 = Professeur("Histoire")
pr1.afficher_matière("histoire & géographie")
pr1.enseigner()