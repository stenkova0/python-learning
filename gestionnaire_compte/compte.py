class Compte:
    def __init__(self, titulaire: str, solde: float = 0) -> None:
        self.titulaire = titulaire
        self.solde = solde

    def __str__(self) -> str:
        return f"{self.titulaire} : {self.solde}"

    def deposer(self, montant: float) -> None:
        self.solde = self.solde + montant

    def retirer(self, montant: float) -> None:
        self.solde = self.solde - montant
        if self.solde < 0:
            self.solde = 0