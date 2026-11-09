from bibliotheque import Bibliotheque
import json

def charger_liste_livre(fichier: str) -> list:
    with open(fichier, "r") as liste_livres:
        livres = json.load(liste_livres)
    
    liste_livres_objet = []
    for chaque_livre in livres:
        liste_livres_objet.append(Bibliotheque(chaque_livre["titre"], chaque_livre["genre"], chaque_livre["auteur"], chaque_livre["notation_personnelle"], chaque_livre["lu"]))
    return liste_livres_objet

def ajouter_un_livre(liste_livres: list, titre: str, genre: str, auteur: str) -> None:
    liste_livres.append(Bibliotheque(titre, genre, auteur))

def afficher_recherche_livre(liste_livres: list, titre: str) -> None:
    for chaque_livre in liste_livres:
        if chaque_livre.titre == titre:
            print(chaque_livre)

def recherche_livre_return(liste_livres: list, titre: str) -> Bibliotheque | None:
    for chaque_livre in liste_livres:
        if chaque_livre.titre == titre:
            return chaque_livre

def sauvegarder_liste_livre(fichier: str, liste_livre : list) -> None:
    liste_livre_dict = []
    for chaque_livre in liste_livre:
        liste_livre_dict.append({"titre": chaque_livre.titre, "genre": chaque_livre.genre, "auteur": chaque_livre.auteur, "notation_personnelle": chaque_livre.notation_perso, "lu": chaque_livre.lu})

    with open(fichier, "w") as fichiers_json:
        json.dump(liste_livre_dict, fichiers_json)