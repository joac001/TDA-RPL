from copy import deepcopy

def vertex_cover_min(grafo, vertices_cubiertos=None, mejor_solucion=None):
    if vertices_cubiertos is None:
        vertices_cubiertos = set()
    if mejor_solucion is None:
        mejor_solucion = set(grafo.obtener_vertices())

    if len(grafo.obtener_vertices()) == 0:
        if len(vertices_cubiertos) < len(mejor_solucion):
            mejor_solucion = vertices_cubiertos
        return list(mejor_solucion)

    vertice = next(iter(grafo.obtener_vertices()))

    # Case 1: vertice is in the cover
    grafo_con_vertice = deepcopy(grafo)
    grafo_con_vertice.borrar_vertice(vertice)
    mejor_solucion = vertex_cover_min(grafo_con_vertice, vertices_cubiertos.union({vertice}), mejor_solucion)

    # Case 2: vertice is not in the cover
    if all(adyacente in vertices_cubiertos for adyacente in grafo.adyacentes(vertice)):
        grafo_sin_vertice = deepcopy(grafo)
        grafo_sin_vertice.borrar_vertice(vertice)
        mejor_solucion = vertex_cover_min(grafo_sin_vertice, vertices_cubiertos, mejor_solucion)

    return list(mejor_solucion)
