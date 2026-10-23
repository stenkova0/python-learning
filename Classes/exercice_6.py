class Joueur:
    def __init__(self, nom, score = 0):
        self.nom = nom
        self.score = score

    def __str__(self):
        return f"{self.nom} : {self.score} points"

    def marquer(self, points):
        self.score = self.score + points

    def afficher(self):
        print(self.score, self.nom)

    def est_meilleur_que(self, autre):
        if self.score > autre.score:
            return True
        else:
            return False

j = Joueur("Alice")
j.afficher()
j.marquer(10)
j.marquer(5)
j.afficher()

liste_joueurs = []

joueurs_A = Joueur("Tristan", 0)
joueurs_A.marquer(5)
liste_joueurs.append(joueurs_A)

joueurs_B = Joueur("Maxence", 10)
joueurs_B.marquer(2)
liste_joueurs.append(joueurs_B)

liste_joueurs.append(Joueur("Alexandra", 15))

for chaque_joueurs in liste_joueurs:
    if chaque_joueurs.score > 10:
        chaque_joueurs.afficher()

a = Joueur("Alice", 15)
b = Joueur("Bob", 10)
print(a.est_meilleur_que(b))
print(b.est_meilleur_que(a))

def trouver_champion(liste_joueurs):
    meilleur_joueur = ""
    meilleur_score = int(0)
    for chaque_joueur in liste_joueurs:
        if chaque_joueur.score > meilleur_score:
            meilleur_score = chaque_joueur.score
    return chaque_joueur

print(trouver_champion(liste_joueurs).nom)

print("-----")

while True:
    print("Bonjour, veuillez choisir une option :\n 1 - Ajouter un joueur\n 2 - Ajouter des points à un joueur\n 3 - Voir le classement\n 4 - Quitter")
    saisi_Menu = input()
    if saisi_Menu == "1":
        print("Veuillez saisir le nom du joueur :")
        saisi_Nom = input()
        print("Veuillez saisir son score :")
        saisi_Score = input()
        #liste_joueurs.append(f"{saisi_Nom, saisi_Score}") < Code de départ. Modifier en ce qui suis à force de voir que les résultats n'étaient pas bon au niveau du formatage
        liste_joueurs.append(Joueur(saisi_Nom, int(saisi_Score)))
        print("-----")
    if saisi_Menu == "2":
        print("Veuillez saisir le nom du joueur :")
        saisi_Nom = input()
        joueur_trouve = ""
        for chaque_joueur in liste_joueurs:
            if saisi_Nom == chaque_joueur.nom:
                print("Veuillez indiqué le nombre de points à lui ajouter :")
                saisi_Score = input()
                chaque_joueur.score = chaque_joueur.score + int(saisi_Score)
                joueur_trouve = "trouvé"

        if joueur_trouve == "":
            print("Ce joueur n'existe pas")
        print("-----")
    if saisi_Menu == "3":
        for chaque_joueur in liste_joueurs:
            print(chaque_joueur)
        print("-----")
    if saisi_Menu == "4":
        break