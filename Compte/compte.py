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