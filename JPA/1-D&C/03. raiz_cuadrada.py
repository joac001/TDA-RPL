def parte_entera_raiz(n):
    if n < 2:
        return n
    
    inicio = 1
    tope = n
    
    while inicio <= tope:
        mitad = (inicio + tope) // 2
        
        if mitad**2 <= n:
            inicio = mitad + 1
        else:
            tope = mitad - 1
    
    return tope

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
