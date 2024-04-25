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
    if (indice == 0): 
        if (alumnos[indice].altura < alumnos[indice + 1].altura):
            return True
    
    elif (indice == len(alumnos)-1):
         if (alumnos[indice].altura < alumnos[indice - 1].altura):
            return True
    
    else:
        if (alumnos[indice].altura < alumnos[indice - 1].altura and alumnos[indice].altura < alumnos[indice + 1].altura):
            return True
    return False