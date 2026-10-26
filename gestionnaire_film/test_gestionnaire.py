from gestionnaire import ajouter_film, chercher_film

def test_ajouter_film():
    liste_film = []
    ajouter_film(liste_film, "Gladiator", "Ridley Scott", 6)
    assert len(liste_film) == 1

def test_chercher_film_existant():
    liste_film = []
    ajouter_film(liste_film, "Gladiator", "Ridley Scott", 6)
    film = chercher_film(liste_film, "Gladiator")
    assert film.titre == "Gladiator"

def test_chercher_film_inexistant():
    liste_film = []
    ajouter_film(liste_film, "Gladiator", "Ridley Scott", 6)
    recherche_film = chercher_film(liste_film, "Interstellar")
    assert recherche_film == None