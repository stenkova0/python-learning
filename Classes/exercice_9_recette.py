class Recette():
    def __init__(self, nom, temps_preparation, facile = True):
        self.nom = nom
        self.temps_preparation = temps_preparation
        self.facile = facile

    def __str__(self):
        return f"{self.nom} | {self.temps_preparation}"

    def est_rapide(self):
        if self.temps_preparation < 30:
            return True
        else:
            return False

liste_recette = []
liste_recette.append(Recette("Gâteau aux pommes", 60))
liste_recette.append(Recette("Smoothie à la banane et au miel", 5))
liste_recette.append(Recette("Pâtes ricotta", 20))

for chaque_recette in liste_recette:
    if chaque_recette.est_rapide() == True:
        print(chaque_recette)