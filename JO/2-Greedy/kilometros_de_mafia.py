def asignar_mafias(pedidos):
    pedidos.sort(key=lambda x: x[1])
    mafias = []
    for pedido in pedidos:
        if not mafias:
            mafias.append(pedido)
        elif pedido[0] > mafias[-1][1]:
            mafias.append(pedido)
    return mafias

# El algoritmo es 2-Greedy porque en cada paso elige la opción óptima localmente, es decir, en cada paso elige el pedido que termina antes.
# El algoritmo no da la solución óptima siempre, ya que no tiene en cuenta el caso en el que un pedido que termina antes, pero que empieza después de otro pedido que termina más tarde, puede ser asignado a una mafia distinta.