def max_grupos_bodegon(P, W):
    #P = [grupo de personas 1, grupo de personas 2]
    #W: lugares en la mesa
    grupos_en_mesa = []
    mejor_grupo = []
    def backtracking(P, W, grupos_en_mesa):
        nonlocal mejor_grupo
        if P is None:
            return
        for grupo in P:
            if grupo <= W:
                W -= grupo
                grupos_en_mesa.append(grupo)
                backtracking(set(P)-{grupo}, W, grupos_en_mesa)
                if sum(grupos_en_mesa) > sum(mejor_grupo):
                    mejor_grupo = grupos_en_mesa.copy()
                elif sum(grupos_en_mesa) == len(mejor_grupo):
                    if len(grupos_en_mesa) > len(mejor_grupo):
                        mejor_grupo = grupos_en_mesa.copy()
                W += grupo
                grupos_en_mesa.pop()
    backtracking(P, W, grupos_en_mesa)
    return mejor_grupo
    
