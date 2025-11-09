from funciones.divisioncaprile import dividir 

def test_dividir(): 
    assert dividir(10, 2) == 5 
    assert dividir(5, 0) is None