# parte_entera_raiz debe devolver la parte entera de la raíz cuadrada de un número n,
# Por ejemplo, para n = 10 debe devolver 3, y para n = 25 debe devolver 5. 
# Complejidad: O(log n)

def parte_entera_raiz(n):
    if n < 2:
        return n
    
    izq, der = 0, n
    
    while der >= izq:
        med = round((izq + der) // 2)
        med_al_cuadrado = med * med
        
        if med_al_cuadrado <= n:
            izq = med + 1
        else:
            der = med - 1
    
    return der

# Ejemplos de uso:
print(parte_entera_raiz(10))  # Salida esperada: 3
print(parte_entera_raiz(25))  # Salida esperada: 5