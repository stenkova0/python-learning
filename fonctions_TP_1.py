#Un professeur veut gérer les notes de sa classe. Il a besoin de pouvoir ajouter un élève avec sa note, voir la liste des élèves qui ont la moyenne (10 ou plus), voir la 
# moyenne de la classe, et quitter.

eleves = [
    {"nom": "Daniel", "note": 12},
    {"nom": "Samantha", "note": 18},
    {"nom": "Jack", "note": 8},
]

while True:
    print("Veuillez choisir votre option :\n 1 - Ajouter un élève avec sa note\n 2 - Voir la liste des élèves qui ont la moyenne\n 3 - Voir la moyenne de la classe\n 4 - Quitter")
    saisi_Menu = input()
    print("------")
    if saisi_Menu == "1":
        print("Saississez le nom de l'élève : ")
        saisi_Nom = input()
        print("Saississez la note de cet élève : ")
        saisi_Note = input()
        eleves.append({"nom": saisi_Nom, "note": int(saisi_Note)})
        print(eleves)
        print("------")
    if saisi_Menu == "2":
        for chaque_Eleves in eleves:
            liste_Eleve_Moyenne = []
            if chaque_Eleves["note"] >= 10:
                liste_Eleve_Moyenne = chaque_Eleves
                print(liste_Eleve_Moyenne)
        print("------")
    if saisi_Menu == "3":
        stockage_Note = int(0)
        moyenne_Classe = int(0)
        nb_Eleves = len(eleves)
        for chaque_Eleves in eleves:
            stockage_Note = stockage_Note + chaque_Eleves["note"]
        moyenne_Classe = stockage_Note / nb_Eleves
        print(moyenne_Classe)
        print("------")
    if saisi_Menu == "4":
        break