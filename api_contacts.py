from fastapi import FastAPI

app = FastAPI()

contacts = [
    {"nom": "Alice", "tel": "0612345678"},
    {"nom": "Bob", "tel": "0698765432"}
]

@app.get("/contacts")
def voir_contacts():
    return contacts

@app.get("/contacts/{nom}")
def chercher_contact(nom: str):
    contact_trouve = ""
    for chaque_contact in contacts:
        if chaque_contact["nom"] == nom:
            contact_trouve = "Oui"
            return chaque_contact
    return {"Erreur": "Contact non trouvé"}