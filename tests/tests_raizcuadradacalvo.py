import unittest
from funciones.raiz_cuadrada import raiz_cuadrada

class TestRaizCuadrada(unittest.TestCase):
    def test_raiz_positiva(self):
        self.assertAlmostEqual(raiz_cuadrada(9), 3.0)

    def test_raiz_cero(self):
        self.assertEqual(raiz_cuadrada(0), 0)

    def test_valor_negativo(self):
        with self.assertRaises(ValueError):
            raiz_cuadrada(-1)

if __name__ == "__main__":
    unittest.main()
