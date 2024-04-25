def indice_primer_cero(arr):
    index_inicio = 0
    index_fin = len(arr) - 1

    if arr[index_inicio] == 0:
        return index_inicio
    
    while index_inicio <= index_fin:
        index_mitad = (index_inicio + index_fin + 1) // 2

        if arr[index_mitad] < arr[index_mitad-1]:
            return index_mitad
        elif arr[index_mitad] == arr[index_mitad-1]:
            if arr[index_mitad] == 0:
                index_fin = index_mitad-1
            else:
                index_inicio = index_mitad+1
    return -1
            
"""
Recordando al Teorema Maestro tenemos que:
aT(n/b)+O(nc)
a = cantidad de llamados recursivos
En este caso, al realizar una iteración, esta permanece en una única instancia, por lo que a = 1
b = proporción del tamaño original con el que se trabaja recursivamente
En este algoritmo de binary search la cantidad parcial de elementos se divide a la mitad por cada iteración, de ahí que b = 2
c = costo de partir y juntar
Al ser la cantidad de operaciones por iteración  constante, c=0

T(n)=T(n/2)+O(1)
como logB(A)= log2(1) = 0 = c
Entonces -> T(n) = O(logn)

"""
