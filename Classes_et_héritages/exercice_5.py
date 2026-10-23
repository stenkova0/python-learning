class Playlist:
    def __init__(self, nom, liste = []):
        self.nom = nom
        self.liste = liste

    def __str__(self):
        taille_liste = len(self.liste)
        return f"{self.nom} : {taille_liste}"

    def ajouter(self, chanson):
        self.liste.append(chanson)

    def duree_totale(self):
        taille_liste = len(self.liste)
        duree_musique = int()
        duree_musique = taille_liste * 3
        return duree_musique

    def duree_en_heures(self):
        duree_musique = self.duree_totale()
        heure = duree_musique // 60
        minute = duree_musique % 60
        return duree_musique, heure, minute


p = Playlist("Rock")
p.ajouter("Highway to Hell")
p.ajouter("Bohemian Rhapsody")
print(p)

p.ajouter("Back in Black")
print(p.duree_totale())   # 9 (3 chansons × 3 minutes)

print(p.duree_en_heures())