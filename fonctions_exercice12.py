livres = [
    {"titre": "1984", "auteur": "Orwell", "lu": True},
    {"titre": "Dune", "auteur": "Herbert", "lu": False},
    {"titre": "Fondation", "auteur": "Asimov", "lu": True},
    {"titre": "Neuromancien", "auteur": "Gibson", "lu": False},
    {"titre": "Solaris", "auteur": "Lem", "lu": False}
]

print("Veuillez indiquer le nom du livre : ")
saisi_Livre = input()

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

print(analyse_livre(livres, saisi_Livre))