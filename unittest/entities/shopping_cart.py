from entities.product import Product

class ShoppingCart:
    
    def __init__(self) -> None:
        # self.__products = list()
        self.__products: List[Product] = []     # anotaciones
        
    @property       # convierte el metodo en un atributo
    def products(self):
        return self.__products.copy()
    
    @property
    def total(self)->float:     # sumar el carrito de compras
        total = [ (product.price - product.discount) for product in self.__products ]
        return sum(total)
        
    def add_product(self, product: Product)-> None:
        self.__products.append(product)
        
    def empty(self) -> bool:
        return len(self.__products) == 0
    
    def has_products(self):
        return not self.empty()
        
    def remove_product(self, product: Product) -> None:
        self.__products.remove(product)