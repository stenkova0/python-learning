class Personnage():
    def __init__(self, nom, points_de_vie = 100):
        self.nom = nom
        self.points_de_vie = points_de_vie

    def __str__(self):
        return f"{self.nom} : {self.points_de_vie}"

    def subir_degats(self, degats):
        self.points_de_vie = self.points_de_vie - degats
        if self.points_de_vie < 0:
            self.points_de_vie = 0


Guerrier_A = Personnage("Alpha")
print(Guerrier_A)
Guerrier_A.subir_degats(50)
print(Guerrier_A)
Guerrier_A.subir_degats(60)
print(Guerrier_A)