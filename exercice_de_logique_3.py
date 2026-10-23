def calculer_note_finale(note, bonus, malus):
    note_final = int()

    note_final = note + bonus - malus
    if note_final > 20:
        note_final = 20

    if note_final < 0:
        note_final = 0

    return note_final

print(calculer_note_finale(15, 3, 1))   # 17
print(calculer_note_finale(18, 5, 1))   # 20 (plafonné)
print(calculer_note_finale(5, 1, 8))    # 0 (plancher)