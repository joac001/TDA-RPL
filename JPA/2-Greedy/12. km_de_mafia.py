# pedidos: lista de tuplas con (km inicio, km fin)
def asignar_mafias(pedidos):    
    if not pedidos:
        return []
    
    pedidos.sort(key=lambda x: x[1])
    permisos_otorgados = [pedidos[0]]
    ultimo_permiso = pedidos[0][1]

    for i in range(1, len(pedidos)):
        inicio, fin = pedidos[i]
        if inicio >= ultimo_permiso:
            permisos_otorgados.append(pedidos[i])
            ultimo_permiso = fin

    return permisos_otorgados

"""
Es un algoritmo Greedy porque va buscando soluciones locales óptimas a fin de obtener una global. En este caso,se pretende evaluar cada pedido según su kilómetro máximo solicitado. De manera ascendente, se van seleccionando los rangos de km de modo que no haya solapamientos. El resultado será una selección optimizada de la cantidad de pedidos.
A diferencia de un algoritmo greedy basado en elegir pedidos de forma lineal o por rangos más chicos, la búsqueda de óptimos locales en base al kilómetro de fin permite una solución mejorada, pero no garantiza que siempre se consiga una solución óptima independientemente del contexto.
En cuanto a la complejidad, en Python, el método sort() tiene una complejidad de tiempo promedio de O(nlogn), siendo n el número de pedidos. A la hora de iterar los pedidos, cada selección de un pedido en sí tiene una complejidad de O(1), siendo la complejidad total de O(n).
"""
