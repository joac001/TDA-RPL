# def buscar_camino_peso_minimo(grafo, inicio):
#     vertices = grafo.obtener_vertices()
#     vertice_actual = inicio
#
#     visitados = [inicio]
#     camino = []
#
#     indice_arista_actual = 0
#     while len(vertices)-1 != len(visitados):
#         if indice_arista_actual == 0:
#             vertice_actual = visitados[-1]
#             aristas = grafo.obtener_aristas(vertice_actual)
#         aristas.sort() # Ordenadas por peso
#
#         if aristas[indice_arista_actual].destino not in visitados and aristas[indice_arista_actual].destino != inicio:
#             visitados.append(aristas[indice_arista_actual].destino)
#             camino.append(aristas[indice_arista_actual])
#             indice_arista_actual = 0
#         else:
#             indice_arista_actual += 1
#
#     aristas_finales = grafo.obtener_aristas(visitados[-1])
#
#     for arista in aristas_finales:
#         if arista.destino == inicio:
#             camino.append(arista)
#     return visitados, camino
#
# def potencia(b,n):
#     if n == 1:
#      return b
#     if n%2 == 0:
#         return potencia(b,n/2)*potencia(b,n/2)
#     else:
#         return potencia(b,n-1)*potencia(b,1)
#
# # Cual es la complejidad del algoritmo potencia(b,n)? justificar la respuesta
# # Respuesta: O(log n) porque en cada llamada a la funcion se divide n por 2 y se llama a la funcion recursivamente
# # hasta llegar a n = 1. Por lo tanto la cantidad de llamadas a la funcion es log(n) + 1, donde log(n) es la cantidad
# # de veces que se puede dividir n por 2 antes de llegar a 1.
#
# def calcular_potencia(b, n):
#     if n == 1:
#         return b
#     if n % 2 == 0:
#         return b*calcular_potencia(b, n // 2)
#     else:
#         return b*calcular_potencia(b, n-1)
#
# # Cual es la complejidad del algoritmo calcular_potencia(b,n)? Respuesta: O(n)
#
# if __name__ == '__main__':
#     print(calcular_potencia(3,3))



# def obtener_dominating_set(arbol):
#     vertices = arbol.obtener_vertices()
#     por_visitar = {}
#     DS = set()
#     for vertice in vertices:
#         por_visitar[vertice] = len(arbol.obtener_aristas(vertice))
#     por_visitar = sorted(por_visitar.items(), key=lambda x: x[1], reverse=True)
#
#     while len(por_visitar) > 0:
#         vertice_actual = por_visitar.pop(0)
#         for vecino in arbol.obtener_vecinos(vertice_actual):
#             # los vecinos incluyen hijos y padre de un nodo
#             if vecino not in DS:
#                 DS.add(vertice_actual)
#     return DS
#

# def backtracking(grafo, vertices, dominating_set_actual, mejor_dominating_set):
#  if len(vertices) == 0:
#         if sum(dominating_set_actual) < sum(mejor_dominating_set):
#             mejor_dominating_set[:] = dominating_set_actual
#         return
#
#     if sum(dominating_set_actual) >= sum(mejor_dominating_set):
#         return
#
#     for vertice in vertices:
#         vecinos = grafo.obtener_vecinos(vertice)
#         for vecino in vecinos:
#             if vecino not in vertices:
#                 dominating_set_actual.append(vertice)
#         backtracking(grafo, set(vertices) - {vertice}, dominating_set_actual, mejor_dominating_set)
#         if (vertice in dominating_set_actual):
#             dominating_set_actual.pop()
#
# def dominating_set_suma_min(grafo):
#     vertices = grafo.obtener_vertices()
#     mejor_dominating_set = vertices[:]
#     dominating_set_actual = []
#     backtracking(grafo, vertices, dominating_set_actual, mejor_dominating_set)
#     return mejor_dominating_set


