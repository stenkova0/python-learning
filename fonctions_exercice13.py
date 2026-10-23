courses = [
    {"article": "Pommes", "quantite": 6, "achete": False},
    {"article": "Pain", "quantite": 1, "achete": True},
    {"article": "Lait", "quantite": 2, "achete": False},
    {"article": "Oeufs", "quantite": 12, "achete": False}
]

while True:
    print("Choissisez votre option :\n 1 - Voir les articles restants à acheter\n 2 - Marquer un article comme acheté\n 3 - Quitter")
    saisi_Menu = input()
    print("------")
    if saisi_Menu == "1" :
        for chaque_Courses in courses:
            if chaque_Courses["achete"] == False:
                print(chaque_Courses)
        print("------")
    if saisi_Menu == "2" :
        print("Veuillez saisir le nom de l'article étant acheté :")
        saisi_Courses = input()
        affichage_Message = ""
        for chaque_Courses in courses:
            if chaque_Courses["article"] == saisi_Courses:
                chaque_Courses["achete"] = True
                affichage_Message = "trouvé"
                print(courses)
        if affichage_Message == "":
            print("Ce produit n'existe pas")
        print("------")
    if saisi_Menu == "3" :
        break