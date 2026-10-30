class Message:
    def __init__(self, expediteur, contenu, lu = False):
        self.expediteur = expediteur
        self.contenu = contenu
        self.lu = lu

    def __str__(self):
        return f"{self.expediteur}\n{self.contenu}\n{self.lu}"

    def lire(self):
        self.lu = True

liste_message = []

message_A = Message("Tristan", "Bonjour, comment vas-tu ?")
message_A.lire()
liste_message.append(message_A)

liste_message.append(Message("Océane", "Tu as reçu mon image ?"))
liste_message.append(Message("Ludwig", "N'oublie pas notre rendez-vous demain !"))

for chaque_message in liste_message:
    if chaque_message.lu == False:
        print(chaque_message)

print("-----")

def demander_nombre(message):
    while True:
        try:
            print(message)
            resultat_demande = int(input())
            return resultat_demande
        except ValueError:
            print("Veuillez saisir un chiffre")

resultat = demander_nombre("Entrez un nombre : ")
print(f"Vous avez tapé {resultat}")
    