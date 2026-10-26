from exercice_9_recette import Recette

def test_est_rapide_20_minutes():
    recette = Recette("Pâtes ricotta", 20)
    assert recette.est_rapide()

def test_est_rapide_40_minutes():
    recette = Recette("Riz au poulet et à la moutarde", 40)
    assert recette.est_rapide() == False