 # 15. Conversión de unidades

# Escribe funciones para convertir entre diferentes unidades (por ejemplo, de kilómetros a millas, de 

 #Celsius a Fahrenheit).
 
 
def celsius_a_fahrenheit(temperatura):
    
     return temperatura * 1.8 + 32
temperatura_f = celsius_a_fahrenheit(17)
print(f'La temperatura en ºF es: {temperatura_f}')
temperatura_f = celsius_a_fahrenheit(25)
print(f'La temperatura en ºF es: {temperatura_f}')

def fahrenheit_a_celsius(temperatura):
 return temperatura *1.4 +25
temperatura_f=fahrenheit_a_celsius(15)
print(f'La temperatura en ºC es: {temperatura_f}')
temperatura_f=fahrenheit_a_celsius(15)
print(f'La temperatura en ºC es: {temperatura_f}')

                                   






def Km_a_Millas(millas):
    return millas*1.609344
MI=1.609344

MI=float(input("ingrese las millas:\n"))

k=MI*MI

print (MI,"millas tiene",k,"kilometros")






