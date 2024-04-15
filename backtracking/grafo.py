import random


class Grafo:
    def __init__(self, dirigido=False, vertices_init=None):
        if vertices_init is None:
            vertices_init = []
        self.dirigido = dirigido
        self.vertices = {v: {} for v in vertices_init}

    def agregar_vertice(self, v):
        if v not in self.vertices:
            self.vertices[v] = {}

    def borrar_vertice(self, v):
        if v in self.vertices:
            del self.vertices[v]
            for vertice in self.vertices:
                self.vertices[vertice].pop(v, None)

    def agregar_arista(self, v, w, peso=1):
        if v in self.vertices and w in self.vertices:
            self.vertices[v][w] = peso
            if not self.dirigido:
                self.vertices[w][v] = peso

    def borrar_arista(self, v, w):
        if v in self.vertices and w in self.vertices:
            self.vertices[v].pop(w, None)
            if not self.dirigido:
                self.vertices[w].pop(v, None)

    def estan_unidos(self, v, w):
        return w in self.vertices[v]

    def peso_arista(self, v, w):
        return self.vertices[v].get(w)

    def obtener_vertices(self):
        return list(self.vertices.keys())

    def vertice_aleatorio(self):
        return random.choice(self.obtener_vertices())

    def adyacentes(self, v):
        return list(self.vertices[v].keys())

    def __str__(self):
        return str(self.vertices)
