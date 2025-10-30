#tests/test_potencia.py 
from funciones.PotenciaMamani import potencia 
def test_potencia(): 
assert potencia(2, 3) == 8 
assert potencia(5, 0) == 1 
