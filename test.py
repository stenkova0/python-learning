#Compréhension de liste

nom = "alice"
print(nom.upper())
print(nom.capitalize())
print(nom.lower())

phrase = "  Bonjour le monde  "
print(phrase.strip())

texte = "Bonjour-le-monde"
print(texte.split("-"))

print("-----")

nombres = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pairs = [n for n in nombres if n % 2 == 0]
print(pairs)

notes = [14, 8, 17, 5, 12, 9, 16]
note_sup_ou_egale_10 = [note for note in notes if note >= 10]
print(note_sup_ou_egale_10)

print("-----")
prenoms = ["alice", "bob", "charlie"]
majuscules = [p.upper() for p in prenoms]
print(majuscules)

print("-----")
notes = [14, 8, 17, 5, 12, 9, 16]
liste_recu_ou_refuser = []
resultats = ["Reçu" if note >= 10 else "Refusé" for note in notes]
print(resultats)

print("-----")

mots = ["python", "code", "apprentissage", "for", "classe", "if"]
mots_P5 = [nb_lettre for nb_lettre in mots if len(nb_lettre) >=5]
print(mots_P5)

print("-----")

eleves = [
    {"nom": "Alice", "note": 14},
    {"nom": "Bob", "note": 8},
    {"nom": "Charlie", "note": 17},
    {"nom": "Diana", "note": 6}
]

eleves_P10 = [nb_eleves["nom"] for nb_eleves in eleves if nb_eleves["note"] >= 10]
print(eleves_P10)

eleves_Note_Double = [notes_eleves["note"] * 2 for notes_eleves in eleves]
print(eleves_Note_Double)

eleves_P10_ND = [notes_eleves["note"] * 2 for notes_eleves in eleves if notes_eleves["note"] >= 10]
print(eleves_P10_ND)

print("-----")
print("-----")
print("-----")

#Décorateurs

def dire_bonjour():
    print("Bonjour !")

def dire_aurevoir():
    print("Au revoir !")

def executer(une_fonction):
    print("Avant")
    une_fonction()
    print("Après")

executer(dire_bonjour)
executer(dire_aurevoir)

print("-----")

def creer_salutation(nom):
    def saluer():
        print(f"Bonjour {nom} !")
    return saluer

salut_alice = creer_salutation("Alice")
salut_bob = creer_salutation("Bob")

salut_alice()
salut_bob()

def ajouter_tirets(fonction):
    def nouvelle_fonction():
        print("-----")
        fonction()
        print("-----")
    return nouvelle_fonction

def masjucules_avant(fonction):
    def nouvelle_fonction():
        print("=== DÉBUT ===")
        fonction()
        print("=== FIN ===")
    return nouvelle_fonction

@ajouter_tirets
@masjucules_avant
def dire_bonjour():
    print("Bonjour !")

#version_amelioree = ajouter_tirets(dire_bonjour)
#version_amelioree()

dire_bonjour()

#---------------------------------------------------
import time

#print(time.time())
#time.sleep(2)
#print(time.time())

def timer_avant(fonction):
    def nouvelle_fonction():
        debut = time.time()
        fonction()
        fin = time.time()
        print(fin-debut)
    return nouvelle_fonction

@timer_avant
def dire_bonjour():
    print("Bonjour !")

dire_bonjour()

@timer_avant
def compter():
    total = 0
    for i in range(10000000):
        total = total + i
    print(total)

print("-----")

def log_avant(fonction):
    def nouvelle_fonction():
        print(f"Appel de {fonction.__name__}")
        fonction()
        print(f"{fonction.__name__} terminé")
    return nouvelle_fonction

@log_avant
def dire_bonjour():
    print("Bonjour !")

dire_bonjour()