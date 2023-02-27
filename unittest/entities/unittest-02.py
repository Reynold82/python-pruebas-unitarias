# En python no se recomiendan las Validaciones, si manejar los Errores

def suma_nros_positivos(n1: int, n2: int) -> int:
    """
    Permite sumar 2 numeros enteros positivos
    Args:
        n1 (int)
        n2 (int)
    Returns:
        int
    """
    assert n1 > 0 and n2 > 0, 'Lo siento, solo se suman nros positivos'
    
    return n1+n2
    
if __name__ == '__main__':
    resultado = suma_nros_positivos(10,20)
    print(resultado)