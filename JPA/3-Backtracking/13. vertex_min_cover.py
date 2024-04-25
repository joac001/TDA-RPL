def vertex_cover_min(grafo):
    mejor_solucion = grafo.obtener_vertices()
    grafo_conexo = False

    def backtracking(vertices, solucion_parcial):
        nonlocal mejor_solucion
        nonlocal grafo_conexo

        if len(vertices) == 0:
            if len(solucion_parcial) < len(mejor_solucion):
                mejor_solucion = solucion_parcial.copy()
            return
        
        if len(solucion_parcial) >= len(mejor_solucion):
            return 

        for vertice in vertices:
            for adyacente in grafo.adyacentes(vertice):
                if adyacente not in solucion_parcial and vertice not in solucion_parcial:
                    grafo_conexo = True
                    solucion_parcial.append(vertice)
            backtracking(set(vertices) - {vertice}, solucion_parcial)
            if vertice in solucion_parcial:
                solucion_parcial.pop()
                        
    solucion_parcial = []
    backtracking(grafo.obtener_vertices(), solucion_parcial)
    return mejor_solucion if grafo_conexo else []
