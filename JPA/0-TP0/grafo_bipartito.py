import sys
# Para el caso de querer implementar un DFS, 
# para que no hayan problemas en la prueba de volumen
sys.setrecursionlimit(10000)

def es_nodo_bipartito(grafo,vertice, visitados, grupo1, grupo2):
    if vertice in grupo2:                   
        return False
    if vertice not in visitados:          
        visitados.add(vertice)            
        grupo1.add(vertice)               
        for adyacente in grafo.adyacentes(vertice):  
            #cada nodo adyacente debe pertenecer al grupo contrario  
            if not es_nodo_bipartito(grafo,adyacente, visitados, grupo2, grupo1):   
                return False
    return True

def es_bipartito(grafo):
    #sabiendo que: un grafo bipartito puede separarse en dos grupos 
    #puedo chequear que para un nodo X, sus adyacentes no pertenezcan a su mismo grupo
    grupo1 = set()
    grupo2 = set()
    visitados = set()

    for vertice in grafo.vertices():
        if vertice not in visitados:
            if not es_nodo_bipartito(grafo,vertice, visitados, grupo1, grupo2):
                return False
            visitados.update(grupo1.union(grupo2))  

    return True
