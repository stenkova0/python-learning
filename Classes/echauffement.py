class Animal:
    def __init__(self, nom, cri):
        self.nom = nom
        self.cri = cri

    def parler(self):
        print(f"{self.nom} fait {self.cri}")

chien_A = Animal("Fido", "waf")
loup_A = Animal("Wulfgard", "aouhhh")
perroquet_A = Animal("Rio", "kwaaah ?")
chien_A.parler()
loup_A.parler()
perroquet_A.parler()

liste_animaux = []
liste_animaux.append(chien_A)
liste_animaux.append(loup_A)
liste_animaux.append(perroquet_A)
print(liste_animaux)

for chaque_Animaux in liste_animaux:
    chaque_Animaux.parler()