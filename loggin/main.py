"""
Los mensajes de consola (tipo console.log en JS) no son muy aceptados en la comunidad pytonica.
En cambio, el modulo 'loggin' nos ayuda de una forma mas profesional

Nos permite trabajar con 5 tipos de mensaje, c/u tienen su nro de prioridad:
 - DEBUG = 10 = debug
 - INFO = 20 = info
 - WARNING = 30 = warning
 - ERROR = 40 = error
 - CRITICAL = 50 = critical

En la funcion basicConfig se setean y formatean los atributos que queremos mostrar.
Ademas, se pueden generar LOGS con filename y filemode.

"""

import logging

logging.basicConfig(level=10,
                    format="%(processName)s - %(levelname)s - %(asctime)s - %(message)s",
                    datefmt="%Y/%m/%d",
                    filename="codigofacilito.log",
                    filemode="a")

def suma(nro1: int, nro2: int) -> int:
    """
    Permite sumar 2 nros enteros

    Args:
        nro1 (int):
        nro2 (int):
    
    Returns:
        :i nt
    """
    logging.debug('Entramos aqui')
    resultado = nro1 + nro2
    logging.debug('Nos encontramos en esta linea')
    return resultado

if __name__ == '__main__':
    logging.debug('Antes del llamado de la funcion')
    resultado = suma(15, 20)
    logging.info(resultado)