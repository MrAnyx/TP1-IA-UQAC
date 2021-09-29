class Graph:
    def __init__(self, nodes={}):
        self.nodes = nodes

    def add_node(self, key, neighbor):
        if not self.nodes[key]:
            self.nodes[key] = [neighbor]

        else:
            self.nodes[key].append(neighbor)
