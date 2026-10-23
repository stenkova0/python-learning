class Livre:
    def __init__(self, titre, auteur, lu = False):
        self.titre = titre
        self.auteur = auteur
        self.lu = lu

    def __str__(self):
        return f"{self.titre} : {self.auteur}"

    def livre_lu(self):
        self.lu = True

liste_livre = []
livre_A = Livre("Blood Ninja", "Nick Lake")
liste_livre.append(livre_A)

livre_B = Livre("Fondation", "Isaac Asimov")
livre_B.livre_lu()
liste_livre.append(livre_B)

livre_C = Livre("Des origines à Auguste", "François Hinard")
liste_livre.append(livre_C)

while True:
    print("Veuillez saisir une option :\n 1 - Ajouter un livre\n 2 - Voir les livres non lus\n 3 - Marquer un livre comme lu\n 4 - Quitter")
    saisi_Menu = input()
    if saisi_Menu == "1":
        print("Veuillez saisir le nom du livre :")
        saisi_Nom_Livre = input()
        print("Veuillez saisir le nom de l'auteur :")
        saisi_Nom_Auteur = input()
        liste_livre.append(Livre(saisi_Nom_Livre, saisi_Nom_Auteur))
        print("-----")
    if saisi_Menu == "2":
        for chaque_livre in liste_livre:
            if chaque_livre.lu == False:
                print(chaque_livre)
        print("-----")
    if saisi_Menu == "3":
        print("Veuillez saisir le nom du livre que vous avez lu :")
        saisi_Nom_Livre = input()
        livre_trouve = ""
        for chaque_livre in liste_livre:
            if chaque_livre.titre == saisi_Nom_Livre:
                chaque_livre.livre_lu()
                livre_trouve = "trouvé"

        if livre_trouve == "":
            print("Ce livre n'existe pas")
        print("-----")
    if saisi_Menu == "4":
        break