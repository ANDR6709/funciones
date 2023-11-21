3.# Diccionario de estudiantes

# Crea un diccionario que almacene información sobre estudiantes (nombre, edad, calificaciones). 

# Escribe funciones para agregar un estudiante, eliminar un estudiante y mostrar la información de

# un estudiante específico.


diccionario = {}

def agregar(diccionario, nombre, edad, calificaciones):
    diccionario[nombre] = {
        'edad': edad,
        'calificaciones': calificaciones
    }

agregar(diccionario, 'Juan', 30, [4.0, 5.0, 3.0])
agregar(diccionario, 'Andres', 20, [5.0, 5.0, 3.0])
agregar(diccionario, 'Pedro', 22, [4.0, 5.0, 4.0])
agregar(diccionario,  'camila',25,[3.0,4.0,5.0])
print(diccionario)

def eliminar(diccionario, nombre):
    if nombre in diccionario:
        del diccionario[nombre]
        print('Estudiante eliminado')
    else:
        print('No se encuentra el nombre')

eliminar(diccionario, 'Nicolas')
print(diccionario)
