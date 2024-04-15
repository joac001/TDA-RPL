import sys
# Para el caso de querer implementar un DFS, 
# para que no hayan problemas en la prueba de volumen

#hay_arista(origen, destino) (devuelve bool), 
#adyacentes(vertice) que devuelve una lista de vértices adyacentes al indicado, 
#nodos() que nos devuelve todos los vértices (lista).

sys.setrecursionlimit(10000)

# Using a Python dictionary to act as an adjacency list
"""grafo = {
    'A' : ['B','C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
}"""
"""
visited = set() # Set to keep track of visited nodes.
colores[vertice] = color

def es_bipartito(grafo):
    for vertice in grafo:
        if vertice not in visited:
            print(vertice)
            vertice.add(vertice)
        for adyacente in grafo[vertice]:
            es_bipartito(grafo)
        


def dfs(visited, graph, node):
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

# Driver Code
dfs(visited, graph, 'A')

"""

def es_nodo_bipartito(grafo, vertice, visitados, grupo_u, grupo_v):
    if vertice in grupo_v:                   
        return False
    if vertice not in visitados:          
        visitados.add(vertice)            
        grupo_u.add(vertice)               
        for adyacente in grafo.adyacentes(vertice):              
            if not es_nodo_bipartito(grafo, adyacente, visitados, grupo_v, grupo_u):   
                return False
    return True

def es_bipartito(grafo):
    grupo_u = set()
    grupo_v = set()
    visitados = set()

    for vertice in grafo.vertices():
        if vertice not in visitados:
            if not es_nodo_bipartito(grafo, vertice, visitados, grupo_u, grupo_v):
                return False
            visitados.update(grupo_u.union(grupo_v))  

    return True

# Ejemplo de uso
grafo_ejemplo = {
    'A': ['B', 'D'],
    'B': ['A', 'C'],
    'C': ['B', 'D'],
    'D': ['A', 'C']
}

resultado = es_bipartito(grafo_ejemplo)
print("El grafo es bipartito:", resultado)
