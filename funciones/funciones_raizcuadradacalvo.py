import math

def raizcuadradacalvo (x):
    """Devuelve la raíz cuadrada de un número positivo x.
    Lanza ValueError si x es negativo."""
    if x < 0:
        raise ValueError("No se puede calcular la raíz cuadrada de un número negativo")
    return math.sqrt(x)
