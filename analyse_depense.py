import json

with open("depense.json", "r") as fichier:
    listeDepense = json.load(fichier)

def voir_depenses(listeDepense):
     return listeDepense

def voir_total_depense(listeDepense):
    stockage_depense = float(0)
    for chaque_Depense in listeDepense:
        stockage_depense = stockage_depense + chaque_Depense["montant"]
    return stockage_depense

def depense_seuil(listeDepense, saisi_Seuil):
    liste_depense = []
    for chaque_Depense in listeDepense:
        if chaque_Depense["montant"] > saisi_Seuil:
            liste_depense.append(chaque_Depense)
    return liste_depense

while True:
    print("Veuillez saisir votre option : \n 1 - Ajouter une dépense\n 2 - Voir toutes les dépenses\n 3 - Voir le total dépensé\n 4 - Voir les dépenses au-dessus d'un montant\n 5 - Sauvegarder et quitter")
    saisi_Menu = input()
    if saisi_Menu == "1":
        print("Veuillez saisir le nom de votre dépense : ")
        saisi_nom_Depense = input()
        print("Veuillez saisir le montant de cette dépense : ")
        saisi_montant_Depense = input()
        listeDepense.append({"nom": saisi_nom_Depense, "montant": float(saisi_montant_Depense)})
        print("------")
    if saisi_Menu == "2":
        print(voir_depenses(listeDepense))
        print("------")
    if saisi_Menu == "3":
        print(voir_total_depense(listeDepense))
        print("------")
    if saisi_Menu == "4":
        print("Veuillez saisir votre montant : ")
        saisi_Seuil = int(input())
        print(depense_seuil(listeDepense, saisi_Seuil))
        print("------")
    if saisi_Menu == "5":
        print("------")
        with open("depense.json", "w") as fichier:
                    json.dump(listeDepense, fichier)
        break