from funciones.sumabenitez import sumabenitez

def test_sumabenitez():
    assert sumabenitez(3, 5) == 8
    assert sumabenitez(-2, 2) == 0
    assert sumabenitez(0, 0) == 0
    assert sumabenitez(10, -3) == 7
