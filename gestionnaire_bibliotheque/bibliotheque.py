class Bibliotheque:
    def __init__(self, titre, genre, auteur, notation_personnelle = 0, lu = False):
        self.titre = titre
        self.genre = genre
        self.auteur = auteur
        self.notation_perso = notation_personnelle
        self.lu = lu

    def __str__(self):
        affichage_lu = "Non lu" if self.lu == False else "Lu"
        return f"{self.titre} | {self.genre} | {self.auteur} | {self.notation_perso} | {affichage_lu}"

    def est_lu(self):
        self.lu = True

    def est_noter(self, note):
        self.notation_perso = note