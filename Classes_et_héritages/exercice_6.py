class Panier():
    def __init__(self, liste_produits = []):
        self.liste_produits = liste_produits

    def ajouter(self, nom, prix):
        self.liste_produits.append({"nom" : nom, "prix": prix})

    def total(self):
        prix_total = int()
        for chaque_produits in self.liste_produits:
            prix_total = prix_total + chaque_produits["prix"] 
        return prix_total

    def total_avec_livraison(self, poids):
        prix_total = self.total()
        prix_avec_livraison = calculer_livraison(poids, 150)
        return prix_total + prix_avec_livraison

def calculer_livraison(poids, distance):
        prix_total = int()
        if distance <= 100:
            prix_total = poids * 2
        else:
            prix_de_base = poids * 2
            pourcentage = prix_de_base * 0.5
            prix_total = prix_de_base + pourcentage
        return prix_total


p = Panier()
p.ajouter("TV", 500)
p.ajouter("Radio", 80)
#print(p.liste_produits)
print(p.total())                    # 580
print(p.total_avec_livraison(10))   # 580 + 30 = 610