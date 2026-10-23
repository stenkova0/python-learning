def partager_addition(total, nb_personnes, pourboire_pct):
    addition_final = float(0)
    pourcentage = float(0)

    pourcentage = total * pourboire_pct / 100
    addition_avec_pourcentage = total + pourcentage
    addition_final = addition_avec_pourcentage / nb_personnes

    return addition_final


print(partager_addition(100, 4, 10))   # 27.5 (100 + 10% = 110, divisé par 4)
print(partager_addition(60, 3, 0))     # 20.0 (pas de pourboire, 60 / 3)