import random

class Vertex:
    def __init__(self, val):
        self.val = val
        self.adjacent = {}
        self.neighbors = []
        self.neighbors_weights = []

    def add_edge(self, vertex, weight=0):
        self.adjacent[vertex] = weight

    def incr_edge(self, vertex):
        self.adjacent[vertex] = self.adjacent.get(vertex, 0) + 1

    def get_probability_map(self):
        for (vertex, weight) in self.adjacent.items():
            self.neighbors.append(vertex)
            self.neighbors_weights.append(weight)

    def next_word(self):
        return random.choices(self.neighbors, weights=self.neighbors_weights)[0]

class Graph:
    def __init__(self):
        self.vertices = {}

    def get_vertex_vals(self):
        return set(self.vertices.keys())

    def add_vertex(self, val):
        self.vertices[val] = Vertex(val)

    def get_vertex(self, val):
        if val not in self.vertices:
            self.add_vertex(val)
        return self.vertices[val]

    def get_next_word(self, curr_vertex):
        return self.vertices[curr_vertex.val].next_word()

    def create_probability_mappings(self):
        for vertex in self.vertices.values():
            vertex.get_probability_map()
    