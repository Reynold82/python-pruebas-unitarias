"""Este es el Dostring del modulo object_doc"""

# Docstring
# __doc__

class User:
    """Permite representar un usuario"""
    
    def __init__(self, username: str, password: str) -> None:
        """Permite instanciar un objeto del  tipo User
        
        Args:
            username (str): El username del usuario.
            password (str): El password del usuario
            
        """
        self.username = username
        self.password = password
        
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
    """
    sentence = sentence.lower().replace(' ','')
    return sentence == sentence[::-1]
    
