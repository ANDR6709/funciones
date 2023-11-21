
8.# Comprobación de palíndromos

# Escribe una función que verifique si una palabra dada es un palíndromo.


from ejercicio4 import invertir

def palindromo(cadena):

    i = cadena

    if isinstance(cadena, int):
        cadena_list = [int(digito) for digito in str(i)]
    else:
        cadena_list = list(cadena)
    
    cadena_inversa = invertir(cadena_list)

    if cadena_list == cadena_inversa:
        return True
    else:
        return False


def palindromo(cadena):

    i = cadena

    if isinstance(cadena, int):
        cadena_list = [int(digito) for digito in str(i)]
    else:
        cadena_list = list(cadena)
    
    cadena_inversa = invertir(cadena_list)

    if cadena_list == cadena_inversa:
        return True
    else:
        return False

prueba1 = 'aerea'
prueba2 = 'sometemos'
prueba3 = 187
prueba4 = 78387
prueba5='oso'
prueba6='arenera'
prueba7='seres'
prueba8="gato"
prueba9="loro"

print(palindromo(prueba1))
print(palindromo(prueba2))
print(palindromo(prueba3))
print(palindromo(prueba4))
print(palindromo(prueba5))
print(palindromo(prueba6))
print(palindromo(prueba7))
print(palindromo(prueba8))
print(palindromo(prueba9))





