class Compte:
    def __init__(self, titulaire, solde = 0):
        self.titulaire = titulaire
        self.solde = solde

    def __str__(self):
        return f"{self.titulaire} : {self.solde}"

    def deposer(self, montant):
        self.solde = self.solde + montant

    def retirer(self, montant):
        self.solde = self.solde - montant

        if self.solde < 0:
            self.solde = 0

class CompteEpargne(Compte):
    def __init__(self, titulaire, solde=0, taux=0.02):
        super().__init__(titulaire, solde)
        self.taux = taux

    def calculer_interets(self):
        self.solde = self.solde + self.solde * self.taux

class CompteCourant(Compte):
    def __init__(self, titulaire, solde=0, decouvert_max = -500):
        super().__init__(titulaire, solde)
        self.decouvert_max = decouvert_max

    def retirer(self, montant):
        self.solde = self.solde - montant
        if self.solde < self.decouvert_max:
            self.solde = self.decouvert_max

a = CompteEpargne("Tristan", 500)
a.calculer_interets()
print(a)

b = CompteCourant("Alice", 200)
b.retirer(300)
print(b)

b = CompteCourant("Alice", 200)
b.retirer(800)
print(b)