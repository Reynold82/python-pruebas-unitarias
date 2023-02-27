import unittest

class TestExample(unittest.TestCase):
    
    def test_suma_numeros(self):
        nro1 = 10
        nro2 = 20
        
        resultado = nro1 + nro2
        self.assertEqual(resultado, 30)
    
    def test_resta_numeros(self):
        self.assertEqual(30 -20, 10)

if __name__ == '__main__':
    unittest.unittest-03()
    
# vamos a la terminal, ejecutamos: python unittest-03.py -v(nos muestra un mensaje de que la prueba unitaria resulto exitosa o no, si no pasa tira un AssertionError)