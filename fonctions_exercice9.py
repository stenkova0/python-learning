films = [
    {"titre": "Matrix", "note": 8.5, "vu": True},
    {"titre": "Inception", "note": 9.0, "vu": True},
    {"titre": "Dune", "note": 7.5, "vu": False},
    {"titre": "Interstellar", "note": 9.2, "vu": False},
    {"titre": "Alien", "note": 8.0, "vu": True}
]

# Étape 1 : Écris une fonction recommandation(films) qui renvoie le titre du film non vu ayant la meilleure note. À toi de décider de la structure.
# Étape 2 : Même liste de films. Écris un petit programme interactif. L'utilisateur tape le titre d'un film. Si le film existe et n'est pas vu, le programme le marque comme 
# vu et affiche un message de confirmation. Si le film est déjà vu, il le dit. Si le film n'existe pas, il le dit aussi.

print("Bonjour veuillez indiquer un nom de film : ")
nom_Film_Saisi = input()

def recommandation(films):

    un_Film = ""
    note_Film = float(0)

    for chaque_Film in films:
        if chaque_Film["vu"] == False:
            if chaque_Film["note"] > note_Film:
                note_Film = chaque_Film["note"]
                un_Film = chaque_Film["titre"]
    return un_Film

def chercher_film(films, titre):  
    for chaque_Film in films:
        if chaque_Film["titre"] == titre:
            return chaque_Film

resultat = chercher_film(films, nom_Film_Saisi)
if resultat != None:
    if resultat["vu"] == False:
        print("Le film n'a pas été vu, il va désormais être mis-à-jour et considéré comme étant vu")
        resultat.update({"vu": True})
    else:
        print("Le film a été vu")
else:
    print("Le film n'existe pas")