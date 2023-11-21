
7.  #Contar elementos únicos

# Escribe una función que tome una lista y devuelva la cantidad de elementos únicos en ella.


lista = [ 'p', 4,'q', 1, 8, 8, 2, 'print', 3, 9, 10, 5, 'q', 'p']

def elementosUnicos(lists):
    i = 0
    while i < len(lists):
        j = i + 1 
        while j < len(lists):
            if lists[i] == lists[j]:
                lists.pop(j)
                lists.pop(i)
                i = 0
                j = i + 1
            else:
                j += 1
        i += 1 
    return(lists)

print(elementosUnicos(lista))
