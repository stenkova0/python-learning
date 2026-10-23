class Vehicule:
    def __init__(self, marque, modele, vitesse = 0):
        self.marque = marque
        self.modele = modele
        self.vitesse = vitesse

    def __str__(self):
        return f"{self.marque} | {self.modele} | Vitesse : {self.vitesse}"

    def vitesse_maximale(self):
        return 130

    def accelerer(self, valeur):
        self.vitesse = self.vitesse + valeur

        if self.vitesse > self.vitesse_maximale():
            self.vitesse = self.vitesse_maximale()

    def freiner(self, valeur):
        self.vitesse = self.vitesse - valeur
        if self.vitesse < 0:
            self.vitesse = 0

class Voiture(Vehicule):
    def __init__(self, marque, modele, portes):
        super().__init__(marque, modele)
        self.portes = portes

    def __str__(self):
        return f"{super().__str__()} | Nombre de portes : {self.portes}"

class Moto(Vehicule):
    def __init__(self, marque, modele, type_permis, vitesse=0):
        super().__init__(marque, modele, vitesse)
        self.type_permis = type_permis

    def __str__(self):
        return f"{super().__str__()} | Type de permis : {self.type_permis}"

    def vitesse_maximale(self):
        return 180

v = Vehicule("Toyota", "Yaris")
print(v)
v.accelerer(50)
print(v)
v.freiner(30)
print(v)
v.freiner(50)
print(v)
print("-----")

# -----

c = Voiture("Peugeot", "308", 5)
print(c)
c.accelerer(80)
print(c)
print(c.vitesse_maximale())
print("-----")

# -----

m = Moto("Yamaha", "R9", "A")
print(m)
m.accelerer(190)
print(m)
print(m.vitesse_maximale())
print("-----")

# -----

vehicules = []
vehicules.append(Voiture("Peugeot", "308", 5))
vehicules.append(Moto("Yamaha", "R9", "A"))
vehicules.append(Voiture("Renault", "Clio", 3))
vehicules.append(Moto("Honda", "CBR", "A2"))

for v in vehicules:
    print(v)