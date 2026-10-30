from note import Note
from gestionnaire import charger_liste, sauvegarder_liste, ajouter_note, chercher_note, saisi_nombre

listes_notes = charger_liste("notes.json")

while True:
    print("Veuillez saisir une option :\n 1 - Ajouter une note\n 2 - Voir toutes les notes\n 3 - Chercher les notes d'une matière\n 4 - Sauvegarder et quitter")
    saisi_Menu = input()
    if saisi_Menu == "1":
        saisi_Note = saisi_nombre("Veuillez saisir une note :")
        print("Veuillez saisir le nom de la matière :")
        saisi_Matiere = input()
        print("Veuillez saisir le contenu de la matière :")
        saisi_Contenu = input()
        ajouter_note(listes_notes, saisi_Note, saisi_Matiere, saisi_Contenu)
        print("-----")
    if saisi_Menu == "2":
        for chaque_notes in listes_notes:
            print(chaque_notes)
        print("-----")
    if saisi_Menu == "3":
        print("Veuillez saisir le nom de la matière :")
        saisi_Matiere = input()
        chercher_note(listes_notes, saisi_Matiere)
        print("-----")
    if saisi_Menu == "4":
        sauvegarder_liste("notes.json", listes_notes)
        print("-----")
        break