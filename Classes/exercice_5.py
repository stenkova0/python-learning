class Chanson:
    def __init__(self, titre, artiste, favori = False):
        self.titre = titre
        self.artiste = artiste
        self.favori = favori

    def afficher_chanson(self):
        print(f"{self.titre} - {self.artiste}")

    def aimer(self):
        self.favori = True

    def est_favori(self):
        return self.favori

liste_chanson = []
chanson_A = Chanson("World of Promises", "Michael Oakley")
chanson_A.aimer()
liste_chanson.append(chanson_A)
chanson_B = Chanson("XXI", "Frequency")
chanson_B.aimer()
liste_chanson.append(chanson_B)
liste_chanson.append(Chanson("I'll Do It", "Voidglitch"))
liste_chanson.append(Chanson("Summer's Ending Soon", "The Midnight"))

for chaque_Chanson in liste_chanson:
    chaque_Chanson.afficher_chanson()

print("-----")

for chaque_Chanson in liste_chanson:
    if chaque_Chanson.est_favori() == True:
        chaque_Chanson.afficher_chanson()