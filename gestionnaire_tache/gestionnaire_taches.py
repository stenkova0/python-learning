import json
from tache import Tache

def charger_taches(fichier):
    with open(fichier, "r", encoding="utf-8") as liste_tache:
        tache = json.load(liste_tache)

    liste_tache_objet = []
    for chaque_tache in tache:
        liste_tache_objet.append(Tache(chaque_tache["titre"], chaque_tache["priorite"], chaque_tache["fait"]))
    return liste_tache_objet

def sauvegarder_taches(fichier, liste_taches):
    list_tache_dict = []
    for chaque_tache in liste_taches:
        list_tache_dict.append({"titre": chaque_tache.titre, "priorite": chaque_tache.priorite, "fait": chaque_tache.fait})

    with open(fichier, "w") as fichier_json:
        json.dump(list_tache_dict, fichier_json)
    
def ajouter_tache(liste_taches, titre, priorite):
    liste_taches.append(Tache(titre, priorite))

def chercher_tache(liste_taches, recherche_tache):
    for chaque_tache in liste_taches:
        if chaque_tache.titre == recherche_tache:
            return chaque_tache