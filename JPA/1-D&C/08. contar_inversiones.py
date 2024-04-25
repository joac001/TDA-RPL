def contar_inversiones(A, B):
    inversiones = [0]  
    merge_sort(B, inversiones)
    return inversiones[0]

def merge(izq, der, inversiones):
    resultado = []
    i = j = 0
    
    while i < len(izq) and j < len(der):
        if izq[i] <= der[j]:
            resultado.append(izq[i])
            i += 1
        else:
            resultado.append(der[j])
            j += 1
            inversiones[0] += len(izq) - i 
    
    resultado.extend(izq[i:])
    resultado.extend(der[j:])
    
    return resultado

def merge_sort(arr, inversiones):
    if len(arr) <= 1:
        return arr

    medio = len(arr) // 2
    split_izq = arr[:medio]
    split_der = arr[medio:]

    izq_ordenado = merge_sort(split_izq, inversiones)
    der_ordenado = merge_sort(split_der, inversiones)

    return merge(izq_ordenado, der_ordenado, inversiones)

"""
Recordando al Teorema Maestro tenemos que:
aT(n/b)+O(nc)
a = cantidad de llamados recursivos
En este caso tenemos 2 llamados recursivos.
b = proporción del tamaño original con el que se trabaja recursivamente
La cantidad de parcial de elementos se divide a la mitad, por lo que b=2
c = costo de partir y juntar
El costo es lineal, por lo que c = 1.

Entonces: T(n)=2T(n/2)+O(n)
como logB(A)= log2(2) = 1 = c
Entonces -> T(n) = O(nlogn) = O(logn)

"""
