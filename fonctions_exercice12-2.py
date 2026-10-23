livres = [
    {"titre": "1984", "auteur": "Orwell", "lu": True},
    {"titre": "Dune", "auteur": "Herbert", "lu": False},
    {"titre": "Fondation", "auteur": "Asimov", "lu": True},
    {"titre": "Neuromancien", "auteur": "Gibson", "lu": False},
    {"titre": "Solaris", "auteur": "Lem", "lu": False}
]

def analyse_livre(livres, saisi):

    affichage_Message = ""

    for chaque_Livre in livres:
        if chaque_Livre["titre"] == saisi:
            if chaque_Livre["lu"] == False:
                affichage_Message = f"Le livre va être dorénavant considéré comme ayant été lu"
                chaque_Livre["lu"] = True
            else:
                affichage_Message = "Ce livre est déjà lu"

    if affichage_Message == "":
        affichage_Message = "Ce livre n'existe pas"
    return affichage_Message

while True:
    print("Veuillez choisir une option :\n 1 - Chercher un livre\n 2 - Voir les livres non lus\n 3 - Quitter\n 4 - Ajouter un livre")
    choix_Menu = input()
    affichage_Message = ""
    if choix_Menu == "1":
        print("Veuillez saisir le nom du livre que vous recherchez")
        choix_Livre = input()
        affichage_Message = analyse_livre(livres, choix_Livre)
        print(affichage_Message)
        print("------")
    if choix_Menu == "2":
        for chaque_Livres in livres:
            if chaque_Livres["lu"] == False:
                affichage_Message = chaque_Livres
                print(affichage_Message)
        print("------")
    if choix_Menu == "3":
        break
    if choix_Menu == "4":
        print("Veuillez indiqué le titre du livre : ")
        titre_du_Film = input()
        print("Veuillez indiqué l'auteur du livre : ")
        auteur_du_Film = input()
        livres.append({"titre": titre_du_Film, "auteur": auteur_du_Film, "lu": False})
        print("------")