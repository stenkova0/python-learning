class Note:
    def __init__(self, note, matiere, contenu):
        self.note = note
        self.matiere = matiere
        self.contenu = contenu

    def __str__(self):
        return f"{self.note} | {self.matiere}. Sujet : {self.contenu}"