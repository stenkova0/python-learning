def calculer_livraison(poids, distance):
    prix_total = int()
    if distance <= 100:
        prix_total = poids * 2
    else:
        prix_de_base = poids * 2
        pourcentage = prix_de_base * 0.5
        prix_total = prix_de_base + pourcentage
    return prix_total

print(calculer_livraison(5, 50))    # 10 (5*2, pas de supplément)
print(calculer_livraison(5, 150))   # 15 (5*2 = 10, + 50% = 15)