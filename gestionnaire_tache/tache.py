class Tache:
    def __init__(self, titre, priorite, fait = False):
        self.titre = titre
        self.priorite = priorite
        self.fait = fait
        
    def __str__(self):
        fait = "✓ Terminée" if self.fait == True else "✗ En cours"
        return  f"{self.titre} | {self.priorite} | {fait}"

    def terminer(self):
        self.fait = True

    def est_urgente(self):
        if self.priorite == "haute":
            return True
        else:
            return False