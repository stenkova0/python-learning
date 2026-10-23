import json

with open("eleves.json", "r") as fichier:
    listeEleves = json.load(fichier)

while True:
    print("Veuillez saisir votre option: \n 1 - Ajouter un élève\n 2 - Voir les élèves au-dessus de la moyenne\n 3 - Voir la moyenne\n 4 - Quitter")
    saisi_Menu = input()

    if saisi_Menu == "1":
        print("Veuillez indiqué le nom de l'élève : ")
        nom_Eleve = input()
        print("Veuillez saisir sa note : ")
        note_Eleve = input()
        listeEleves.append({"nom": nom_Eleve, "note": int(note_Eleve)})
        with open("eleves.json", "w") as fichier:
            json.dump(listeEleves, fichier)
        print("------")
    if saisi_Menu == "2":
        liste_eleve_Moy = []
        for chaque_Eleve in listeEleves:
            if chaque_Eleve["note"] >= 10:
                liste_eleve_Moy = chaque_Eleve
                print(liste_eleve_Moy)
        print("------")
    if saisi_Menu == "3":
        stockage_Moyenne = float(0)
        moyenne = float(0)
        taille_liste_Eleve = len(listeEleves)
        for chaque_Eleve in listeEleves:
            stockage_Moyenne = stockage_Moyenne + chaque_Eleve["note"]
        moyenne = stockage_Moyenne/taille_liste_Eleve
        print(moyenne)
        print("------")
    if saisi_Menu == "4":
        break