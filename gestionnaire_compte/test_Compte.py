from compte import Compte

def test_retirer_deposer_500():
    client_A = Compte("Tristan", 1000)
    client_A.deposer(500)
    assert client_A.solde == 1500