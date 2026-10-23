class Equipe():
    def __init__(self, nom, liste_joueurs = []):
        self.nom_equipe = nom
        self.liste_joueurs = liste_joueurs

    def ajouter(self, nom, score):
        self.liste_joueurs.append({"nom": nom, "score": score})

    def meilleur_joueur(self):
        meilleur_score = int(0)
        nom_meilleur_joueur = ""
        for chaque_joueur in self.liste_joueurs:
            if chaque_joueur["score"] > meilleur_score:
                meilleur_score = chaque_joueur["score"]
                nom_meilleur_joueur = chaque_joueur["nom"]
        return f"{nom_meilleur_joueur}, dont le score est de : {meilleur_score}"

    def moyenne(self):
        moyenne_score = float(0)
        taille_liste = len(self.liste_joueurs)
        for chaque_joueur in self.liste_joueurs:
            moyenne_score = moyenne_score + chaque_joueur["score"]
        moyenne_score_total = moyenne_score / taille_liste
        return moyenne_score_total

    def resume(self):
        meilleur_joueur = self.meilleur_joueur()
        moyenne = self.moyenne()
        print(f"Équipe : {self.nom_equipe} | Meilleur(se) joueur(se) : {meilleur_joueur} | Moyenne : {moyenne}")



e = Equipe("Rock")
e.ajouter("Alice", 50)
e.ajouter("Bob", 20)
e.ajouter("Charlie", 20)
e.resume()