class Graph:
    def __init__(self, oriented=False):
        self.oriented = oriented
        self.nodes = []
        self.edges = []  

    def add_node(self, node):
        if node not in self.nodes:
            self.nodes.append(node)

    def add_edge(self, u, v, weight=None):
        self.add_node(u)
        self.add_node(v)
        self.edges.append([u, v, weight])

    def remove_node(self, node):
        if node in self.nodes:
            self.nodes.remove(node)
        
        new_edges = []
        for h in self.edges:
            if h[0] != node and h[1] != node:
                new_edges.append(h)
        self.edges = new_edges

    def remove_edge(self, u, v):
        for h in self.edges:
            if self.oriented:
                if h[0] == u and h[1] == v:
                    self.edges.remove(h)
                    break
            else:
                if (h[0] == u and h[1] == v) or (h[0] == v and h[1] == u):
                    self.edges.remove(h)
                    break

    def get_neighbors(self, node):
        neighbors = []
        for h in self.edges:
            if h[0] == node:
                if h[1] not in neighbors:
                    neighbors.append(h[1])
            elif not self.oriented and h[1] == node:
                if h[0] not in neighbors:
                    neighbors.append(h[0])
        return neighbors

    def analyze(self):
        print("--- ANALYZA GRAFU ---")
        node_cnt = len(self.nodes)
        edge_cnt = len(self.edges)
        print("Pocet uzlu:", node_cnt)
        print("Pocet hran:", edge_cnt)

        # 1. oriented
        if self.oriented:
            print("oriented: Ano")
        else:
            print("oriented: Ne")

        rated = False
        for h in self.edges:
            if h[2] is not None:
                rated = True
                break
        if rated:
            print("rated: Ano")
        else:
            print("rated: Ne")

        cyclic = False
        for h in self.edges:
            if h[0] == h[1]:
                cyclic = True
                break
        if cyclic:
            print("Ma smycky: Ano")
        else:
            print("Ma smycky: Ne")

        continuous = True
        if node_cnt > 0:
            visited = [self.nodes[0]]
            queue = [self.nodes[0]]

            while len(queue) > 0:
                current = queue.pop(0)
                for h in self.edges:
                    neighbor = None
                    if h[0] == current:
                        neighbor = h[1]
                    elif h[1] == current:
                        neighbor = h[0]
                    
                    if neighbor is not None and neighbor not in visited:
                        visited.append(neighbor)
                        queue.append(neighbor)

            if len(visited) != node_cnt:
                continuous = False

        if continuous:
            print("continuous: Ano")
        else:
            print("continuous: Ne")

        planar = True
        if node_cnt >= 3:
            if edge_cnt > (3 * node_cnt - 6):
                planar = False
        if planar:
            print("planar: Ano")
        else:
            print("planar: Ne")

        if cyclic:
            print("Chromaticke cislo: Nelze urcit (graf ma smycky)")
        elif node_cnt == 0:
            print("Chromaticke cislo: 0")
        else:
            colors = {} 
            for node in self.nodes:
                used_colors = []

                for h in self.edges:
                    neighbor = None
                    if h[0] == node and h[1] != node:
                        neighbor = h[1]
                    elif h[1] == node and h[0] != node:
                        neighbor = h[0]
                    
                    if neighbor in colors:
                        used_colors.append(colors[neighbor])

                color = 1
                while color in used_colors:
                    color += 1
                colors[node] = color

            max_color = max(colors.values())
            print("Chromaticke cislo:", max_color)
        print("---------------------\n")


if __name__ == "__main__":
    g = Graph(oriented=False)
    
    g.add_edge("A", "B", 10)
    g.add_edge("B", "C", 5)
    g.add_edge("C", "A", 8)
    g.add_edge("C", "D", 12)

    g.analyze()

    g2 = Graph(oriented=True)
    g2.add_edge(1, 2)
    g2.add_edge(2, 2)  
    g2.analyze()