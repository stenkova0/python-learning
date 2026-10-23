def rendre_monnaie(prix,paye):
    if prix == paye:
        print("Le compte est exact")

    if paye > prix:
        rend_argent = int(0)
        rend_argent = paye - prix
        print(f"Vous m'avez donné trop ! Je vous rends {rend_argent}")

    if paye < prix:
        argent_supp = int(0)
        argent_supp = prix - paye
        print(f"Vous ne m'avez pas donné assez ! Vous me devez encore {argent_supp}")

rendre_monnaie(30, 50)  # "Rendu : 20"
rendre_monnaie(30, 20)  # "Il manque : 10"
rendre_monnaie(30, 30)  # "Compte exact"
print("-----")

def calculer_remise(prix, quantite):
    if quantite >= 10:
        prix = prix * quantite
        calcule_remise = prix * 0.2
        prix = prix - calcule_remise
    else:
        prix = prix * quantite
    return prix

print(calculer_remise(5, 3))    # 15 (pas de remise)
print(calculer_remise(5, 12))   # 48 (60 - 20%)
print("-----")

def calculer_facture(prix, quantite, credit):
    prix = prix * quantite
    if credit > prix:
        credit = credit - prix
        print(f"Vous n'avez rien à payer, il vous reste {credit}")
    else:
        prix = prix - credit
        print(f"Vous me devez {prix}")
    return prix, credit

calculer_facture(10, 3, 20)   # à payer: 10, crédit restant: 0
calculer_facture(10, 3, 50)   # à payer: 0, crédit restant: 20