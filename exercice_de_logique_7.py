def calculer_ht(quantite, prix_unitaire):
    prix_ht = quantite * prix_unitaire
    return prix_ht

def calculer_tva(montant_ht, taux):
    montant_TVA = montant_ht * taux / 100
    return montant_TVA

def generer_facture(quantite, prix_unitaire, taux):
    prix_ht = calculer_ht(quantite, prix_unitaire)
    tva = calculer_tva(prix_ht, taux)
    facture = prix_ht + tva
    return print(facture)

generer_facture(5, 10, 20)