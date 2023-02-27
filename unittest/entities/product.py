# mediante clases podemos crear nuestros propios errores

class ProductDiscountError(Exception):
        pass

class Product:

    def __init__(self, name: str, price: float, discount: float = 0.0) -> None:
        self.name = name
        self.price = price
        self.discount = discount
        
        if discount > price:
            raise ProductDiscountError('El descuento no puede ser mayor al precio')
    
    # EVALUAR EXPRESIONES REGULARES
    @property
    def code(self):
        # este metodo simula la creacion de un codigo
        return f'code-{self.name}'
    