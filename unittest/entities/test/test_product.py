import unittest

from entities.product import Product

class TestProduct(unittest.TestCase):
    
    def setUp(self):
        print('>>>el metodo setUp se ejecuta antes de c/u de las pruebas')
        self.name = 'iPhone'
        self.price = 500.00
        self.smartphone = Product(self.name, self.price)
    
    
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
    
   
if __name__ == '__main__':
    unittest.main()
    
