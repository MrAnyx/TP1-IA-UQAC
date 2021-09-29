class Processor:
    def __init__(self, robot):
        self.robot = robot

    def get_room_coords_from_id(self, id):
        return [math.floor(id / 5), id % 5]

    def get_room_id_from_coords(self, coords):
        return coords[0] + (coords[1] * 5)

    def get_neighbor_rooms(self, current):
        neighbor = []
        if current[0] > 0:
            neighbor.append([current[0] - 1, current[1]])  # [x-1, y]

        if current[0] < 4:
            neighbor.append([current[0] + 1, current[1]])  # [x+1, y]

        if current[1] > 0:
            neighbor.append([current[0], current[1] - 1])  # [x, y-1]

        if current[1] < 4:
            neighbor.append([current[0], current[1] + 1])  # [x, y+1]

        return neighbor

    def create_graph(self):
        """
        Renvoie un dictionnaire de type :
        {
            "node_id" : [neighbors_id]
            ...
        }
        """
        graph = {}
        for i in range(5):
            for j in range(5):
                neighbors = self.get_neighbor_rooms([i, j])
                id = i + 5 * j
                neighbors_ids = list(
                    map(lambda el: self.get_room_id_from_coords(el), neighbors)
                )

                graph[id] = neighbors_ids

        return graph

    # Exploration non informée
    # Peut-être envisager le depth-limited deepening ou le depth first search
    def depth_first_search(self):
        pass

    # Exploration informée avec une heuristique (norme entre deux cases)
    def greedy_search(self):
        pass
