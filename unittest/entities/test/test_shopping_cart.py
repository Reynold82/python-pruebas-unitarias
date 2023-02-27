import unittest
from entities.product import Product
from entities.product import ProductDiscountError
from entities.shopping_cart import ShoppingCart

def is_available_to_skip():
    # cuando la conexion a la bdd no puede establecerse
    # si pongo False, la prueba se ejecuta
    return True

def is_connected():
    # funcion para seaber si hay una conexion establecida
    return False

class TestShoppingCart(unittest.TestCase):
    
    # SETUP & TEARDOWN: Podemos definir acciones que se ejecuten antes o despues de cada una de las pruebas.
    # Aqui podemos definir todo lo necesario para lleavr a cabo las pruebas. En comun, con SetUp podemos inicializar nuestros objetos para ser usados en las pruebas unitarias. Y en tearDown, simplemente reestablecemos estos objetos
    
    @classmethod
    def setUpClass(cls):
        print('>>>el metodo de clase setUpClass se ejecuta antes de c/u de las pruebas')
        # por ejemplo, podria ser una clase para conexion a una BDD
        
    @classmethod
    def tearDownClass(cls):
        print('>>>el metodo de clase tearDownClass se ejecuta antes de c/u de las pruebas')
        
    def setUp(self):
        print('>>>el metodo setUp se ejecuta antes de c/u de las pruebas')
        self.name = 'iPhone'
        self.price = 500.00
        self.smartphone = Product(self.name, self.price)
        
        self.shopping_cart_1 = ShoppingCart()
        self.shopping_cart_2 = ShoppingCart()
        
        self.shopping_cart_2.add_product(self.smartphone)
    
    def tearDown(self):
        print('>>>el metodo setUp se ejecuta despues de c/u de las pruebas')
        
    def test_product_object(self):
        name = 'Manzana'
        price = 1.70
        
        product = Product(name, price)
        
        self.assertEqual(product.name, name)
        self.assertEqual(product.price, price, 'Lo siento, precio incorrecto')
    
    def test_product_name(self):
        self.assertEqual(self.smartphone.name, self.name)
    
    def test_product_price(self):
        self.assertEqual(self.smartphone.price, self.price)
    
    def test_shopping_cart_empty(self):
        self.assertTrue(self.shopping_cart_1.empty(), 'Carrito Vacio!')
    
    def test_shopping_cart_has_product(self):
        self.assertTrue(self.shopping_cart_2.has_products())    # asserTrue, assertFalse
        self.assertFalse(self.shopping_cart_2.empty())
    
    def test_product_in_shopping_cart(self):
        product = Product('Nuevo Producto', 10)
        self.shopping_cart_2.add_product(product)
        
        self.assertIn(product, self.shopping_cart_2.products)
        self.assertIn(self.smartphone, self.shopping_cart_2.products)    # assertIn busca si un objeto está en una colección
    
    def test_product_not_in_shopping_cart(self):
        self.shopping_cart_2.remove_product(self.smartphone)
        self.assertNotIn(self.smartphone, self.shopping_cart_2.products)
    
    def test_discount_error(self):      
        with self.assertRaise(ProductDiscountError):        # assertRaise, lanza errores creados por nosotros mediante clases
            Product(name='Example', price=10.0, discount=11.0)
    
    def test_total_shopping_cart(self):
        self.shopping_cart_1.add_product(Product(name='Libro', price=15.0))
        self.shopping_cart_1.add_product(Product(name='Camara', price=700.0, discount=70.0))
        
        self.assertGreater(self.shopping_cart_1.total, 0)        # assertGreater, nos permite evaluar mayor que '>'
        self.assertLess(self.shopping_cart_1.total, 1000)        # assertLess, nos permite evaluar menor que '<'
        
        self.assertEqual(self.shopping_cart_1.total, 645)
        # assertGreaterEqual, mayor igual
        # assertLessEqual, menor igual
    
    def test_total_empty_shopping_cart(self):
        self.assertEqual(self.shopping_cart_1.total, 0.0)
    
    # SALTAR PRUEBAS(sobre valores booleanos): cuando el desarrollador sabe que la prueba no puede ser ejecutada
    
    # skip
    @unittest.skip('la prueba no cumple con los requisitos necesarios')
    def test_skip_example(self):
        self.assertEqual(1,1)
    
    # SALTAR PRUEBAS(sobre valores booleanos): cuando el desarrollador NO sabe que la prueba no puede ser ejecutada
    
    # skipIf - evalua sobre verdadero
    @unittest.skipIf(is_available_to_skip(), 'no se cuenta con todos los requisitos')
    def test_skip_example_two(self):
        pass
    
    # skipUnless - evalua sobre falso
    @unittest.skipUnless(is_connected(), 'no se encuentra conexion')
    def test_skip_example_three(self):
        pass
    
    def test_code_product(self):
        self.assertRegex(self.smartphone.code, self.smartphone.name) # regEx, 1er string, 2do substring que coincida con el 1ero.
        # self.assertRegex(self.smartphone.code, 'codigo facilito', 'el codigo no cumple con la expresion')
    
    
if __name__ == '__main__':
    unittest.main()
    
# vamos a la terminal e ingresamos: python test_shopping_cart -v