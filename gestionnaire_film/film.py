class Film:
    def __init__(self, titre, realisateur, note, vu = False):
        self.titre = titre
        self.realisateur = realisateur
        self.note = note
        self.vu = vu

    def __str__(self):
        return f"{self.titre} : {self.note} | {self.realisateur} | {self.vu}"

    def est_recommande(self):
        if self.note > 7:
            return True
        else:
            return False

    def marquer_vu(self):
        self.vu = True