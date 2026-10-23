class Film:
    def __init__(self, titre, realisateur, note):
        self.titre = titre
        self.realisateur = realisateur
        self.note = note

    def __str__(self):
        return f"{self.titre} : {self.note} | {self.realisateur}"

    def est_recommande(self):
        if self.note > 7:
            return True
        else:
            return False


liste_film = []
liste_film.append(Film("Troie", "Wolfgang Petersen", 14))
liste_film.append(Film("Transformers", "Michael Bay", 14))
liste_film.append(Film("Le Jour d'après", "Roland Emmerich", 6))

for chaque_film in liste_film:
    film_recommande = chaque_film.est_recommande()
    if film_recommande == True:
        print(chaque_film)