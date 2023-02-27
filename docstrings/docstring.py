# Docstring
__doc__

def palindromo(sentence: str) -> bool:
    """
    Permite conocer si un string es o no un palindromo
    
    Args:
        sentence: string
        
    Returns:
        bool
    
    Example:
    >>> palindromo('Anita lava la tina')
    True
    >>> palindromo('CodigoFacilito')
    False
    >>> sentence = 'Oso'
    >>> palindromo(sentence)
    False
    """
    sentence = sentence.lower().replace(' ','')
    return sentence == sentence[::-1]


# Ejecutando la shell de Python podemos ver como quedó documentado nuestro programa, de dos maneras:
# >>>palindromo.__doc__     o
# >>>help(palindromo)

# Extension: autoDocstring. Funciona cuando escribimos triple comillas dobles

##########################

# Doctest: 

# Permite probar nuestro codigo. Tenemos que ingresar ">>>" seguido de un ejemplo. Luego en la terminal: python -m main.py -v. PERO NO ES UN SOFTWARE DE TESTEO, es solo para documentar objetos.
