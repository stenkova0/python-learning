from gestionnaire import ajouter_film, chercher_film
from film import Film

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

def test_verification_recommandation_neuf():
    liste_film = []
    ajouter_film(liste_film, "Gladiator", "Ridley Scott", 9)
    recherche_film = chercher_film(liste_film, "Gladiator")
    verification = Film.est_recommande(recherche_film)
    assert verification == True

def test_verification_recommandation_cinq():
    liste_film = []
    ajouter_film(liste_film, "Gladiator", "Ridley Scott", 5)
    recherche_film = chercher_film(liste_film, "Gladiator")
    verification = Film.est_recommande(recherche_film)
    assert verification == False

def test_verification_marquage():
   liste_film = []
   ajouter_film(liste_film, "Gladiator", "Ridley Scott", 5)
   recherche_film = chercher_film(liste_film, "Gladiator")
   recherche_film.marquer_vu()
   assert recherche_film.vu == True