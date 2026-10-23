from gestionnaire import charger_films, sauvegarder_films, ajouter_film, chercher_film

affichage_liste = charger_films("films.json")

while True:
    print("Veuillez saisir une option :\n 1 - Voir la liste des films\n 2 - Ajouter un film\n 3 - Chercher un film\n 4 - Sauvegarder et quitter")
    saisi_Menu = input()
    if saisi_Menu == "1":
        for chaque_film in affichage_liste:
            print(chaque_film)
        print("-----")
    if saisi_Menu == "2":
        print("Veuillez saisir le titre du film :")
        saisi_Titre_Film = input()
        
        print("Veuillez saisir le nom de son réalisateur :")
        saisi_Nom_Realisateur = input()
        
        print("Veuillez indiqué la note de ce film :")
        saisi_Note_Film = int(input())
        ajouter_film(affichage_liste, saisi_Titre_Film, saisi_Nom_Realisateur, saisi_Note_Film)
        
        print("-----")
    if saisi_Menu == "3":
        print("Veuillez saisir le titre du film que vous recherchez :")
        saisi_Titre_Film_Recherche = input()
        recherche_Film = chercher_film(affichage_liste, saisi_Titre_Film_Recherche)

        if recherche_Film == None:
            print("Ce film n'existe pas")
        else:
            print(recherche_Film)

        print("-----")
    if saisi_Menu == "4":
        sauvegarder_films("films.json", affichage_liste)
        print("-----")
        break