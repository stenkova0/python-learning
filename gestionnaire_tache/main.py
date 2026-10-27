from gestionnaire_taches import charger_taches, sauvegarder_taches, ajouter_tache, chercher_tache
from tache import Tache

affichage_liste_taches = charger_taches("taches.json")

while True:
    print("Veuillez saisir une des options :\n 1 - Ajouter une tâche\n 2 - Voir les tâches non terminées\n 3 - Voir les tâches urgentes\n 4 - Terminer une tâche\n 5 - Sauvegarder et quitter")
    saisi_Menu = input()
    
    if saisi_Menu == "1":
        print("Veuillez saisir le titre de la tâche :")
        saisi_Titre_Tache = input()
        print("Veuillez saisir la priorité de la tâche (haute, moyenne, basse) :")
        saisi_Priorite_Tache = input()
        ajouter_tache(affichage_liste_taches, saisi_Titre_Tache, saisi_Priorite_Tache)
        print("-----")
    if saisi_Menu == "2":
        for chaque_tache in affichage_liste_taches:
            if chaque_tache.fait == False:
                print(chaque_tache)
        print("-----")
    if saisi_Menu == "3":
        for chaque_tache in affichage_liste_taches:
            if chaque_tache.est_urgente():
                print(chaque_tache)
        print("-----")
    if saisi_Menu == "4":
        print("Veuillez indiquer le titre de la tâche terminer :")
        saisi_Tache_Terminer = input()
        tache_trouver = ""

        for chaque_tache in affichage_liste_taches:
            if chaque_tache.titre == saisi_Tache_Terminer:
                chaque_tache.terminer()
                tache_trouver = "trouvé"

        if tache_trouver == "":
            print("Cette tâche n'existe pas")
    
        print("-----")
    if saisi_Menu == "5":
        sauvegarder_taches("taches.json", affichage_liste_taches)
        print("-----")
        break