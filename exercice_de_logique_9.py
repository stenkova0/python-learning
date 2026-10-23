def calculer_prix_reduit(prix, reduction_pct):
    montant_reduction = prix * reduction_pct / 100
    prix_apres_reduction = prix - montant_reduction
    return prix_apres_reduction

def trouver_bonnes_affaires(produits, seuil):
    for chaque_produits in produits:
        prix_apres_reduction = calculer_prix_reduit(chaque_produits["prix"], chaque_produits["reduction"])
        if prix_apres_reduction <= seuil:
            print(chaque_produits["nom"])

produits = [
    {"nom": "TV", "prix": 500, "reduction": 20},
    {"nom": "Radio", "prix": 80, "reduction": 10},
    {"nom": "Casque", "prix": 100, "reduction": 50}
]

trouver_bonnes_affaires(produits, 100)
# TV : 400 → trop cher
# Radio : 72 → bonne affaire
# Casque : 50 → bonne affaire