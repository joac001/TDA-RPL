alumnos = [1.2, 1.15, 1.14, 1.12, 1.10, 1.09, 1.02, 0.98, 1.18, 1.23]

"""
1ER PIVOTE: 10//2 = 5 -> 1.09
1.09 < 1.10? si
me quedo con la parte derecha a partir de 1.09
2DO PIVOTE : 5//2 = 2 -> 0.98
0.98 < 1.02? si
me quedo con la parte derecha a partir de 0.98
3ER PIVOTE: 3//2 = 1 -> 1.18
1.18 < 0.98? no
me quedo con la parte izquierda sin incluir a 1.18
4TO PIVOTE: 1//1 = 1 -> 0.98
len() = 1? LO ENCONTRÉ!

alumnos = [1.2, 1.15, 1.14, 1.18, 1.23, 1.45, 1.54, 2.08, 3.10]
1ER PIVOTE: 9//2 = 4 -> 1.23
1.23 < 1.18? no
me quedo con la parte izquierda sin incluir a 1.23
2DO PIVOTE: 4//2 = 2 -> 1.14
1.14 < 1.15? si
me quedo con la parte derecha a partir de 1.14
3ER PIVOTE: 2//2 = 1 -> 1.18
1.18 < 1.14? no
me quedo con la parte izquierda sin incluir a 1.18
4TO PIVOTE: 1//1 = 1 -> 1.14
len() = 1? LO ENCONTRÉ! 

alumnos = [1.2, 1.17, 1.15, 1.01, 1.02, 1,02, 1.03, 1.04, 1.05, 1.06]
1ER PIVOTE: 10//2 = 5 -> 1.02
1.02 <= 1.02? si
me quedo con la parte derecha




"""
def indice_mas_bajo(alumnos):
    index_inicio = 0
    index_fin = len(alumnos) - 1

    while index_inicio < index_fin:
        index_mitad = (index_inicio + index_fin) // 2

        if alumnos[index_mitad] > alumnos[index_mitad + 1]:
            index_inicio = index_mitad + 1
 
        else:
            index_fin = index_mitad

    return index_inicio



def validar_mas_bajo(alumnos, indice):
    if 0 < indice < len(alumnos) - 1:
        return alumnos[indice] < alumnos[indice + 1] and alumnos[indice] < alumnos[indice - 1]
    return False
    

indice = indice_mas_bajo(alumnos)
print("El índice del alumno más bajo es:", indice)
print("La altura del alumno más bajo es:", alumnos[indice])

print(validar_mas_bajo(alumnos,0))
print(validar_mas_bajo(alumnos,9))
print(validar_mas_bajo(alumnos,7))
print(validar_mas_bajo(alumnos,12))
print(validar_mas_bajo(alumnos,-1))

"""
def indice_mas_bajo(alumnos, offset=0):
    index_pivote = len(alumnos) // 2
    numero_pivote = alumnos[index_pivote]
    if len(alumnos) == 1:
        return index_pivote + offset
    
    elif numero_pivote == alumnos[index_pivote-1]:
        del alumnos[index_pivote]
        return indice_mas_bajo(alumnos, offset)
    
    elif numero_pivote < alumnos[index_pivote - 1]:
        return indice_mas_bajo(alumnos[index_pivote:], offset + index_pivote)
    
    else:
        return indice_mas_bajo(alumnos[:index_pivote], offset)

"""