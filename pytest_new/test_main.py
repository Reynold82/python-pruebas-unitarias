import pytest
# para realizar pruebas unitarias con pytest se antepone "test_"

# def test_example():
#    assert 10 == 20, 'La prueba no ha pasado'

# se recomienda agrupar las pruebas en un mismo contexto

class TestExample():

    @classmethod
    def setup_class(cls):
        print('>>> setup_class se ejecuta antes de todas las pruebas')
    @classmethod
    def teardown_class(cls):
        print('>>> setup_class se ejecuta despues de todas las pruebas')
 
    def setup_method(self):
        # el metodo setup se ejecuta antes de cada prueba
        self.nro_uno = 20
        self.nro_dos = 20

    def teardown_method(self):
        # el metodo teardown se ejecuta despues de cada prueba
        pass

    def test_suma_dos_nros(self):
        assert self.nro_uno + self.nro_dos == 40, 'Lo siento, suma incorrecta'
    
    def test_resta_dos_nros(self):
        assert self.nro_uno - self.nro_dos == 0, 'Lo siento, resta incorrecta'

""" class TestExample2():

    def test_multip_dos_nros(self):
        assert 2 * 10 == 20 """

# para ejecutar todas las pruebas: pytest -v
# para ejecutar una prueba en especifico: pytest test_main.py::TestExample::test_resta_dos_nros -v
# para ejecutar pruebas de una clase en especifico: pytest test_main.py::TestExample -v
