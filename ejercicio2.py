2. # Verificar paridad

# Escribe una función que tome un número como argumento y devuelva un mensaje indicando si es 

# par o impar.


def paresImpares(numero):
    if (numero % 2) == 0:
        print('El numero', numero, 'es par')
    else: 
        print('El numero', numero, 'es impar')

paresImpares(2)
paresImpares(3)
paresImpares(4)
paresImpares(5)

