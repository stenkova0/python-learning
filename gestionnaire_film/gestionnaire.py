import json
from film import Film

def charger_films(fichier):
    with open(fichier, "r", encoding="utf-8") as liste_film:
        films = json.load(liste_film)

    list_film_objet = []
    for chaque_film in films:
        list_film_objet.append(Film(chaque_film["titre"], chaque_film["realisateur"], chaque_film["note"], chaque_film["vu"]))

    return list_film_objet

def sauvegarder_films(fichier, liste_films):
    list_film_dict = []
    for chaque_film in liste_films:
        list_film_dict.append({"titre": chaque_film.titre, "realisateur": chaque_film.realisateur, "note": chaque_film.note, "vu": chaque_film.vu})

    with open(fichier, "w") as fichier_json:
        json.dump(list_film_dict, fichier_json)

def ajouter_film(liste_films, titre, realisateur, note):
    liste_films.append(Film(titre, realisateur, note))

def chercher_film(liste_films, titre):
    for chaque_film in liste_films:
        if chaque_film.titre == titre:
            return chaque_film