from note import Note
import json

def charger_liste(fichier):
    with open(fichier, "r", encoding="utf-8") as notes:
        listes_notes = json.load(notes)

    liste_des_notes_objet = []
    for chaque_note in listes_notes:
        liste_des_notes_objet.append(Note(chaque_note["Note"], chaque_note["Matière"], chaque_note["Contenu"]))

    return liste_des_notes_objet

def ajouter_note(liste, note, matiere, contenu):
    liste.append(Note(note, matiere, contenu))

def chercher_note(liste, matiere):
    for chaque_note in liste:
        if chaque_note.matiere == matiere:
            print(chaque_note)

def saisi_nombre(message):
    while True:
        try:
            print(message)
            saisi_nombre = int(input())
            return saisi_nombre
        except ValueError:
            print("Veuillez saisir un chiffre")

def sauvegarder_liste(fichier, liste):
    liste_des_notes_dictionnaire = []
    for chaque_note in liste:
        liste_des_notes_dictionnaire.append({"Note": chaque_note.note, "Matière": chaque_note.matiere, "Contenu": chaque_note.contenu})

    with open(fichier, "w") as fichiers_json:
        json.dump(liste_des_notes_dictionnaire, fichiers_json)
