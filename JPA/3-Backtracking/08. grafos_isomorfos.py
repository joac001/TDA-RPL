#Implementar un algoritmo de backtracking que, dados dos grafos, determine si existe un Isomorfismo entre ambos.

def imagen_cumple_isomorfismo(g2, adyacentes, vertices_espejo):
    for vertice2 in g2.obtener_vertices():
        if len(adyacentes) == len(g2.adyacentes(vertice2)) and vertice2 not in vertices_espejo:
            return True
    return False

def backtracking(g1, vertices_dominio, g2, vertices_espejo):
    #vertices dominio: los vertices a los que quedan buscar imagen en el grafo 2
    #vertices espejo: vertice de g2 descubierto como posible imagen de un vertice en g1
    if len(vertices_espejo) == len(g1.obtener_vertices()):
        return True
    for vertice in vertices_dominio:
        if imagen_cumple_isomorfismo(g2, g1.adyacentes(vertice), vertices_espejo):
            vertices_espejo.add(vertice)
            if backtracking(g1, set(vertices_dominio) - {vertice},g2, vertices_espejo):
                return True
            vertices_espejo.remove(vertice)
    return False



def hay_isomorfismo(g1, g2):
    vertices_espejo = set()
    if len(g1.obtener_vertices()) != len(g2.obtener_vertices()):
        return False
    return backtracking(g1, g1.obtener_vertices(), g2, vertices_espejo)
    





