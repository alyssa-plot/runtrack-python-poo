class Operation:
    def __init__(self, nombre1, nombre2):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

    def resultat(self):
        print(self.nombre1 + self.nombre2)

operation1 = Operation(3, 12)
operation1.resultat()
