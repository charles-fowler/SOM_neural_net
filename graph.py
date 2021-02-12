class Vertex(object):
    def __init__(self,node):
        self.id = node
        self.adj = {}

    def __str__(self):
        return str(self.id) + ' adjacent: ' + str([x.id for x in self.adj])

    def add_neighbor(self, neighbor, weight=0):
        self.adj[neighbor] = weight

    def get_connections(self):
        return self.adj

    def get_id(self):
        return self.id

    def get_weight(self, neighbor):
        return self.adj[neighbor]


class Graph:
    def __init__(self):
        self.vertices = {}
        self.num_vertices = 0

    def __str__(self):
        return str(x for x in self.vertices) + str(self.num_vertices)

    def __iter__(self):
        return iter(self.vertices.values())

    def add_vertex(self, node):
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(node)
        self.vertices[node] = new_vertex
        return new_vertex

    def get_vertex(self, n):
        if n in self.vertices:
            return self.vertices[n]
        else:
            return None

    def add_edge(self, frm, to, cost=0):
        if frm not in self.vertices:
            self.add_vertex(frm)
        if to not in self.vertices:
            self.add_vertex(to)

        self.vertices[frm].add_neighbor(self.vertices[to], cost)
        self.vertices[to].add_neighbor(self.vertices[frm], cost) # adds to both vertices

    def get_vertices(self):
        return self.vertices.keys()



def generate_square_map(rows,columns):  # square with no diagonals
    g = Graph()
    for r in rows:
        for c in columns:
            g.add_vertex(str(r + c))

    for r in rows: # column to column connectors
        for ct,cf in zip(columns[:-1],columns[1:]): #ct = column to and rf = row from etc.
            #print(r+ct+"-->"+r+cf)
            g.add_edge(str(r+ct),str(r+cf),1)

    for c in columns: # row to row connectors
        for rf,rt in zip(rows[:-1],rows[1:]):
            #print(rf+c+"-->"+rt+c)
            g.add_edge(str(rf+c),str(rt+c),1)

    return g


def generate_triangular_map(rows,columns):  # right leaning parallelogram
    g = Graph()
    for r in rows:
        for c in columns:
            g.add_vertex(str(r + c))

    for r in rows:  # pure column to column connectors
        for ct, cf in zip(columns[:-1], columns[1:]):
            # print(r+ct+"-->"+r+cf)
            g.add_edge(str(r + ct), str(r + cf), 1)

    for rf, rt in zip(rows[:-1], rows[1:]): # down a column connectors (diagonal right)
        for c in columns:
            # print(rf+c+"-->"+rt+c)
            g.add_edge(str(rf + c), str(rt + c), 1)

    for rf,rt in zip(rows[1:],rows[:-1]):
        for cf, ct in zip(columns[:-1], columns[1:]):
            g.add_edge(str(rf + cf), str(rt + ct), 1)

    return g



graph = generate_triangular_map(["A", "B", "C", "D", "E"],["1", "2", "3", "4"])
p = graph.get_vertices()
print(p)

a = graph.get_vertex("B2")
print(a)












