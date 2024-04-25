def indice_mas_bajo(alumnos):
    index_inicio = 0
    index_fin = len(alumnos) - 1

    while index_inicio < index_fin:
        index_mitad = (index_inicio + index_fin) // 2

        if alumnos[index_mitad].altura > alumnos[index_mitad + 1].altura:
            index_inicio = index_mitad + 1
 
        else:
            index_fin = index_mitad

    return index_inicio



def validar_mas_bajo(alumnos, indice):
    if 0 < indice < len(alumnos) - 1:
        return alumnos[indice].altura < alumnos[indice + 1].altura and alumnos[indice].altura < alumnos[indice - 1].altura
    return False
