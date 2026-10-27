from produit import Produit

def test_vendre_3():
    p = Produit("Clavier", 45, 10)
    p.vendre(3)
    assert p.quantite_stock == 7

def test_vendre_20():
    p = Produit("Clavier", 45, 10)
    p.vendre(20)
    assert p.quantite_stock == 0