def additionner(a: int, b: int) -> int:
    return a + b

print(additionner(5, 3))
print(additionner("hello", "world"))

def calculer_moyenne(notes: list, moyenne: float = 0) -> float:
    nb_notes = len(notes)
    total_note = int(0)
    for chaque_notes in notes:
        total_note = total_note + chaque_notes
        moyenne = total_note / nb_notes
    return moyenne

def est_majeur(age: int) -> bool:
    if age >= 18:
        return True
    else:
        return False

def chercher_nom(personnes: list, nom: str) -> str | None:
    for chaque_personne in personnes:
        if chaque_personne == nom:
            return chaque_personne