def charlas(horarios):
    if not horarios:
        return []
    
    horarios.sort(key=lambda x: x[1])
    charlas = [horarios[0]]
    ultima_charla = horarios[0][1]

    for i in range(1, len(horarios)):
        inicio, fin = horarios[i]
        if inicio >= ultima_charla:
            charlas.append(horarios[i])
            ultima_charla = fin

    return charlas

    """
Es un algoritmo Greedy porque va buscando soluciones locales óptimas a fin de obtener una global. En este caso,se pretende evaluar cada charla según su horario de finalizacióón. De manera ascendente, se van seleccionando las charlas de modo que no hayan solapamiento. El resultado será una selección optimizada de la cantidad de charlas.

En cuanto a la complejidad, en Python, el método sort() tiene una complejidad de tiempo promedio de O(nlogn), siendo n el número de charlas. A la hora de iterar las charlas, cada selección de una charla en sí tiene una complejidad de O(1), siendo la complejidad total de O(n).
"""
