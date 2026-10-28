from compte import Compte

def test_retirer_0():
    client_A = Compte("Tristan", 50)
    client_A.retirer(100)
    assert client_A.solde == 0