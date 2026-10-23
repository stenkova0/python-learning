produits = [
    {"nom": "Pain", "prix": 1.20},
    {"nom": "Caviar", "prix": 45.00},
    {"nom": "Lait", "prix": 0.95},
    {"nom": "Champagne", "prix": 38.00},
    {"nom": "Eau", "prix": 0.50}
]

def est_cher(prix):
    return prix > 10

def produits_chers(produits):
    liste_Produit_Cher = []
    prix_total = float(0)
    for chaque_Produit in produits:
        if est_cher(chaque_Produit["prix"]) == True:
            liste_Produit_Cher.append(chaque_Produit["nom"])
            prix_total = prix_total + chaque_Produit["prix"]
    return liste_Produit_Cher, prix_total

print(produits_chers(produits))