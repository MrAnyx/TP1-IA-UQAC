class Graph:
    def __init__(self, nodes={}):
        self.nodes = nodes

    def add_node(self, key, neighbor):
        if key not in self.nodes:
            self.nodes[key] = [neighbor]

        else:
            self.nodes[key].append(neighbor)

    def get_node_neighbors(self, key):
        if key not in self.nodes:
            return None

        return self.nodes[key]
