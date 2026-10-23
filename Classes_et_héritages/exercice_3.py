class Personnage:
    def __init__(self, nom, points_de_vie = 100):
        self.nom = nom
        self.points_de_vie = points_de_vie

    def __str__(self):
        return f"{self.nom} : {self.points_de_vie}"

    def attaquer(self):
        return f"{self.nom} attaque !"

    def subir_degats(self, degats):
        self.points_de_vie = self.points_de_vie - degats
        if self.points_de_vie < 0:
            self.points_de_vie = 0

class Guerrier(Personnage):
    def __init__(self, nom, points_de_vie=100, armure = 20):
        self.armure = armure
        super().__init__(nom, points_de_vie)

    def subir_degats(self, degats):
        degats = degats - self.armure
        if degats < 0:
            degats = 0

        self.points_de_vie = self.points_de_vie - degats

        if self.points_de_vie < 0:
            self.points_de_vie = 0

class Mage(Personnage):
    def __init__(self, nom, points_de_vie=100, bouclier = 50):
        self.bouclier = bouclier
        super().__init__(nom, points_de_vie)

    def subir_degats(self, degats):
        if degats <= self.bouclier:
            self.bouclier = self.bouclier - degats
        else:
            reste = degats - self.bouclier
            self.bouclier = 0
            self.points_de_vie = self.points_de_vie - reste

        if self.points_de_vie < 0:
            self.points_de_vie = 0

p = Personnage("Guerrier")
print(p)
p.subir_degats(30)
print(p)
p.subir_degats(90)
print(p)

print("-----")

g = Guerrier("Thor")
print(g)
g.subir_degats(50)
print(g)
g.subir_degats(10)
print(g)

print("-----")

m = Mage("Merlin")
print(m)
m.subir_degats(30)
print(m)
m.subir_degats(40)
print(m)