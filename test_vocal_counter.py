from vocalcounter import *
import unittest

class Testscontadorvoacles(unittest.TestCase):
    def test_cantidad_vocales_nula(self):
        palabra = 'tttt'
        palabras_contadas = contadorvocales(palabra)
        self.assertEqual ({'a':0, 'e':0, 'i':0, 'o':0, 'u':0}, palabras_contadas)
    def test_cantidad_vocales_1(self):
        palabra = 'sol'
        palabras_contadas = contadorvocales(palabra)
        self.assertEqual ({'a':0, 'e':0, 'i':0, 'o':1, 'u':0}, palabras_contadas)
    def test_cantidad_vocales_2(self):
        palabra = 'casa'
        palabras_contadas = contadorvocales(palabra)
        self.assertEqual ({'a':2, 'e':0, 'i':0, 'o':0, 'u':0}, palabras_contadas)
    def test_cantidad_vocales_todasunavez(self):
        palabra = 'aeiou'
        palabras_contadas = contadorvocales(palabra)
        self.assertEqual ({'a':1, 'e':1, 'i':1, 'o':1, 'u':1}, palabras_contadas)
    def test_sin_vocales(self):
        palabra = "tryhgf"
        resultado = contadorvocales(palabra)
        self.assertEqual(resultado, {'a':0, 'e':0, 'i':0, 'o':0, 'u':0})
    def test_con_vocal_o(self):
        palabra = "sol"
        resultado = contadorvocales(palabra)
        self.assertEqual(resultado, {'a':0, 'e':0, 'i':0, 'o':1, 'u':0})
    def test_con_vocal_doble_o(self):
        palabra = "solo"
        resultado = contadorvocales(palabra)
        self.assertEqual(resultado, {'a':0, 'e':0, 'i':0, 'o':2, 'u':0})
    def test_con_dos_vocales(self):
        palabra = "sola"
        resultado = contadorvocales(palabra)
        self.assertEqual(resultado, {'a':1, 'e':0, 'i':0, 'o':1, 'u':0})
    def test_con_todas_las_vocales(self):
        palabra = "solamente quiero que gane Boca"
        resultado = contadorvocales(palabra)
        self.assertEqual(
            resultado,
            {"a": 3, "e": 5, "i": 1, "o": 3, "u": 2},
        )
    def test_con_vocales_en_mayuscula(self):
        palabra = "SOlAmente quIerO"
        resultado = contadorvocales(palabra)
        self.assertEqual(
            resultado,
            {"a": 1, "e": 3, "i": 1, "o": 2, "u": 1},
        )

if __name__ == '__main__':
    unittest.main()