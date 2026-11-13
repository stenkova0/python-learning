from fastapi import FastAPI
from pydantic import BaseModel
import json

def charger_contacts(fichier):
    with open(fichier, "r") as liste_contacts:
        lc = json.load(liste_contacts)
        return lc

contacts = charger_contacts("liste_contacts.json")

app = FastAPI()

class ContactModel(BaseModel):
    nom: str
    tel: str

@app.get("/contacts")
def voir_contacts():
    return contacts

@app.get("/contacts/{nom}")
def chercher_contact(nom: str):
    for chaque_contact in contacts:
        if chaque_contact["nom"] == nom:
            return chaque_contact
    return {"Erreur": "Contact non trouvé"}

@app.post("/contacts")
def ajouter_contact(contact: ContactModel):
    contacts.append({"nom": contact.nom, "tel": contact.tel})
    sauvegarde_contacts("liste_contacts.json", contacts)
    return {"message": f"Contact {contact.nom} ajouté"}

@app.delete("/contacts/{nom}")
def supprimer_contact(nom: str):
    for chaque_contact in contacts:
        if chaque_contact["nom"] == nom:
            contacts.remove(chaque_contact)
            sauvegarde_contacts("liste_contacts.json", contacts)
            return f"L'utilisateur {chaque_contact['nom']} a été supprimé"
    return {"Erreur": "Contact non trouvé"}

@app.put("/contacts/{nom}")
def modifier_contact(nom: str, telephone_new: ContactModel):
    for chaque_contact in contacts:
        if chaque_contact["nom"] == nom:
            chaque_contact["tel"] = telephone_new.tel
            sauvegarde_contacts("liste_contacts.json", contacts)
            return chaque_contact
    return {"Erreur": "Contact non trouvé"}

def sauvegarde_contacts(fichier, liste_contacts):
    with open(fichier, "w") as fichier_contact:
        json.dump(liste_contacts, fichier_contact)