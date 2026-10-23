class Tache:
    def __init__(self, titre, fait = False):
        self.titre = titre
        self.fait = fait

    def afficher(self):
        if self.fait == True:
            print(f"{self.titre} - ✓")
        else:
            print(f"{self.titre} - ✗")

    def terminer(self):
        self.fait = True

t = Tache("Faire les courses")
t.afficher()
t.terminer()
t.afficher()

print("-----")

liste_tache = []
liste_tache.append(Tache("Faire le ménage", True))
liste_tache.append(Tache("Faire la lessive"))
liste_tache.append(Tache("Faire la poussière"))
liste_tache.append(Tache("Faire les courses"))

print("-----")

while True:
    print("Bonjour veuillez choisir une option :\n 1 - Ajouter une tâche\n 2 - Voir les tâches non terminées\n 3 - Terminer une tâche\n 4 - Quitter")
    saisi_Menu = input()

    if saisi_Menu == "1":
        print("Veuillez saisir le nom de la tâche :")
        saisi_Tache = input()
        liste_tache.append(Tache(saisi_Tache))
        print("-----")
    if saisi_Menu == "2":
        for chaque_Tache in liste_tache:
            if chaque_Tache.fait == False:
                chaque_Tache.afficher()
        print("-----")
    if saisi_Menu == "3":
        print("Veuillez indiqué la tâche qui a été effectuée :")
        saisi_Tache_Effectue = input()
        affichage_message = ""
        for chaque_Tache in liste_tache:
            if saisi_Tache_Effectue == chaque_Tache.titre:
                chaque_Tache.terminer()
                print(f"La tâche {saisi_Tache_Effectue} a été changé en 'terminé'")
                affichage_message = "trouvé"

        if affichage_message == "":
            print("Cette tâche n'existe pas")
        print("-----")
    if saisi_Menu == "4":
        break