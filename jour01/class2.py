class Operation:
    def __init__(self, nombre1, nombre2):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

    def resultat(self):
        print(f"{self.nombre1} {self.nombre2}")

operation1 = Operation("Le nombre1 est", 12)
operation2 = Operation("Le nombre2 est", 3)

operation1.resultat()
operation2.resultat()