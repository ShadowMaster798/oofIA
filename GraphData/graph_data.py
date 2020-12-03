class Vertex:
    def __init__(self, name, coordinates: list):
        self.name = name
        self.coordinates = coordinates

    def aerial_distance(self, destination_coords: list):
        """TODO Implementar cálculos"""

class Edge:
    def __init__(self, estimated_time):
        self.estimated_time = estimated_time
