def dominating_set_min(grafo):
    solucion_optima = grafo.obtener_vertices()

    def do_backtracking(vertices, optima_local):
        nonlocal solucion_optima

        if len(vertices) == 0:
            if len(optima_local) < len(solucion_optima):
                solucion_optima = optima_local.copy()
            return

        if len(optima_local) >= len(solucion_optima):
            return

        for vertice in vertices:
            if vertice not in optima_local:
                adyacentes = grafo.adyacentes(vertice)
                do_backtracking(set(vertices) - {vertice} - set(adyacentes), optima_local + [vertice])

    solucion_optima_local = []
    do_backtracking(grafo.obtener_vertices(), solucion_optima_local)
    return solucion_optima
