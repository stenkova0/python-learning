import json

class Jeu():
    def __init__(self, titre, heure_joue):
        self.titre = titre
        self.heure_joue = heure_joue

    def __str__(self):
        return f"{self.titre} : {self.heure_joue}"

with open("jeux.json", "r") as liste_jeux:
    jeux = json.load(liste_jeux)
    liste_jeux_objet = []
    for chaque_jeux in jeux:
        liste_jeux_objet.append(Jeu(chaque_jeux["titre"], chaque_jeux["heures"]))

while True:
    print("Veuillez choisir votre option :\n 1 - Ajouter un jeu\n 2 - Voir mes jeux\n 3 - Sauvegarder et quitter")
    saisi_Menu = input()
    if saisi_Menu == "1":
        print("Veuillez saisir le nom du jeu : ")
        saisi_Nom_Jeu = input()
        print("Veuillez indiqué votre temps de jeu : ")
        saisi_Heure_Joue = input()
        liste_jeux_objet.append(Jeu(saisi_Nom_Jeu, saisi_Heure_Joue))
        print("-----")
    if saisi_Menu == "2":
        for chaque_jeu in liste_jeux_objet:
            print(chaque_jeu)
        print("-----")
    if saisi_Menu == "3":
        liste_jeux_dict = []
        for chaque_jeu in liste_jeux_objet:
            liste_jeux_dict.append({"titre": chaque_jeu.titre, "heures": chaque_jeu.heure_joue})
        with open("jeux.json", "w") as fichier:
            json.dump(liste_jeux_dict, fichier)
        break