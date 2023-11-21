# 13. Verificación de números primos

# Escribe una función que verifique si un número dado es primo.


def Primo(numero):
    es_primo = True
    if numero > 1:
        for i in range(2, int(numero**0.5) + 1):
            if numero % i == 0:
                es_primo = False
                break

    if es_primo and numero > 1:
        print(f"{numero} es un número primo.")
    else:
        print(f"{numero} no es un número primo.")

Primo(12)
Primo(3)
Primo(20)
Primo(5)
Primo(14)
Primo(15)
Primo(19)
Primo(23)
Primo(29)
