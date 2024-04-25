def vertex_cover_min(grafo):
    grafo_conexo = False
    solucion_optima = grafo.obtener_vertices()

    def do_backtracking(vertices, optima_local):
        nonlocal solucion_optima
        nonlocal grafo_conexo

        if len(vertices) == 0:
            if len(optima_local) < len(solucion_optima):
                solucion_optima = optima_local.copy()
            return

        if len(optima_local) >= len(solucion_optima):
            return

        for vertice in vertices:
            for adyacente in grafo.adyacentes(vertice):
                if adyacente not in optima_local and vertice not in optima_local:
                    grafo_conexo = True
                    optima_local.append(vertice)
            do_backtracking(set(vertices) - {vertice}, optima_local)
            if vertice in optima_local:
                optima_local.pop()

    solucion_optima_local = []
    do_backtracking(grafo.obtener_vertices(), solucion_optima_local)
    return solucion_optima if grafo_conexo else []
