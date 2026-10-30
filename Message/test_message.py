from message import Message

def test_message_lu():
    message_A = Message("Océane", "Tu as reçu mon image ?")
    message_A.lire()
    assert message_A.lu == True