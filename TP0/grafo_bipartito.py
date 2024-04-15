import sys
# Para el caso de querer implementar un DFS, 
# para que no hayan problemas en la prueba de volumen

#hay_arista(origen, destino) (devuelve bool), 
#adyacentes(vertice) que devuelve una lista de vértices adyacentes al indicado, 
#vertices() que nos devuelve todos los vértices (lista).

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

def es_nodo_bipartito(grafo, vertice, visitados, grupo1, grupo2):
    if vertice in grupo2:                   
        return False
    if vertice not in visitados:          
        visitados.add(vertice)            
        grupo1.add(vertice)               
        for adyacente in grafo[vertice]:              
            if not es_nodo_bipartito(grafo, adyacente, visitados, grupo2, grupo1):   
                return False
    return True

def es_bipartito(grafo):
    #Sabiendo que: un grafo bipartito puede separarse en dos grupos 
    #tal que para cada par de vértices de un grupo no exista arista entre sí 
    grupo1 = set()
    grupo2 = set()
    visitados = set()

    for vertice in grafo:
        if vertice not in visitados:
            if not es_nodo_bipartito(grafo, vertice, visitados, grupo1, grupo2):
                return False
            visitados.update(grupo1.union(grupo2))  

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
