class Compteur:
    def __init__(self):
        self.valeur = 0

    def incrementer(self):
        self.valeur = self.valeur + 1

    def afficher(self):
        print(self.valeur)

mon_compteur = Compteur()
mon_compteur.afficher()
mon_compteur.incrementer()
mon_compteur.incrementer()
mon_compteur.incrementer()
mon_compteur.afficher()