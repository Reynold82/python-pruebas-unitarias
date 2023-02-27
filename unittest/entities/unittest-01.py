# Pruebas Unitarias:
    # " EN PYTHON ES MEJOR MANEJAR LOS ERRORES"

# assert: lanza un error si no es True

if __name__ == '__main__':
    try:
        assert 5 == 10, 'Lo siento, 5 no es igual a 10'
        print('>>> El programa continua con su ejecucion')
    except AssertionError as error:
        print(error)