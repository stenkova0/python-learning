class Eleve:
    def __init__(self, nom, note):
        self.nom = nom
        self.note = note

    def est_recu(self):
        if self.note >= 10 :
            return True
        else:
            return False

    def bonus(self, points):
        self.note = self.note + points

    def afficher(self):
        if self.est_recu() == True:
            print(f"L'élève {self.nom} a eu la note de {self.note} et est reçu")
        else:
            print(f"L'élève {self.nom} a eu la note de {self.note} et est refusé")
        


eleve_A = Eleve("Tristan", 5)
print(eleve_A.note)
eleve_B = Eleve("Marianne", 10)
eleve_C = Eleve("Endmin", 15)
liste_Eleve = []
liste_Eleve.append(eleve_A)
liste_Eleve.append(eleve_B)
liste_Eleve.append(eleve_C)

for chaque_Eleve in liste_Eleve:
    chaque_Eleve.afficher()