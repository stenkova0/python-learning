from calculs import additionner

def test_additionner():
    assert additionner(2, 3) == 5

def test_additionner_negatif():
    assert additionner(-1, -1) == -2