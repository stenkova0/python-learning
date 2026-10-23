class Produit:
    def __init__(self, nom, prix):
        self.nom = nom
        self.prix = prix

    def appliquer_reduction(self, pourcentage):
        prix_Avant = self.prix * pourcentage / 100
        self.prix = self.prix - prix_Avant

    def afficher(self):
        print(self.nom, self.prix)

    def est_gratuit(self):
        if self.prix <= 0:
            return True
        else:
            return False

p = Produit("Casque", 100)
p.afficher()
p.appliquer_reduction(20)
p.afficher()

p = Produit("Souris", 50)
p.afficher()
p.appliquer_reduction(20)
print(p.est_gratuit())
p.afficher()

p = Produit("Clavier", 70)
p.afficher()
p.appliquer_reduction(100)
print(p.est_gratuit())
p.afficher()

print("--------")

tshirt = Produit("T-shirt", 50)
tshirt.appliquer_reduction(10)

debardeur = Produit("Débardeur", 30)
debardeur.appliquer_reduction(100)

jean = Produit("Jean", 80)
jean.appliquer_reduction(5)

liste_produit = []
liste_produit.append(tshirt)
liste_produit.append(debardeur)
liste_produit.append(jean)

for chaque_produit in liste_produit:
    chaque_produit.est_gratuit()
    if chaque_produit.est_gratuit() == False:
        chaque_produit.afficher()