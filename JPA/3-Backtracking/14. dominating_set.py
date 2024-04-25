def dominating_set_min(grafo):
    mejor_solucion = grafo.obtener_vertices()

    def backtracking(vertices, solucion_parcial):
        nonlocal mejor_solucion

        if len(vertices) == 0:
            if len(solucion_parcial) < len(mejor_solucion):
                mejor_solucion = solucion_parcial.copy()
            return
        
        if len(solucion_parcial) >= len(mejor_solucion):
            return 

        for vertice in vertices:
            al_menos_un_adyacente_en_D = False
            for adyacente in grafo.adyacentes(vertice):
                if adyacente in solucion_parcial:
                    al_menos_un_adyacente_en_D = True
            if not al_menos_un_adyacente_en_D:
                solucion_parcial.append(vertice)
            backtracking(set(vertices) - {vertice}, solucion_parcial)
            if vertice in solucion_parcial:
                solucion_parcial.pop()
                        
    solucion_parcial = []
    backtracking(grafo.obtener_vertices(), solucion_parcial)
    return mejor_solucion
