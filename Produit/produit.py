class Produit:
    def __init__(self, nom, prix, quantite_stock):
        self.nom = nom
        self.prix = prix
        self.quantite_stock = quantite_stock

    def __str__(self):
        return f"{self.nom} : {self.prix} | {self.quantite_stock}"

    def est_disponible(self):
        if self.quantite_stock > 0:
            return True
        else:
            return False

    def vendre(self, quantite):
        self.quantite_stock = self.quantite_stock - quantite
        if self.quantite_stock < 0:
            self.quantite_stock = 0

p = Produit("Clavier", 45, 10)
print(p)
p.vendre(3)
print(p)
p.vendre(20)
print(p)