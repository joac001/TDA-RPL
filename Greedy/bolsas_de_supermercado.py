def bolsas(capacidad, prductos):
    bolsas = []
    prductos.sort(reverse=True)

    for i in prductos:
        if len(bolsas) == 0:
            bolsas.append([i])
        else:
            for j in bolsas:
                if sum(j) + i <= capacidad:
                    j.append(i)
                    break
            else:
                bolsas.append([i])
    return bolsas

# El algoritmo implementado encuentra siempre la solución óptima porque se ordenan los productos de mayor a
# menor y se van agregando a la bolsa que tenga espacio disponible, si no hay bolsas disponibles se crea una nueva bolsa.