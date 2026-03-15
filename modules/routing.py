import heapq

class Graph:

    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v, weight):

        if u not in self.graph:
            self.graph[u] = []

        if v not in self.graph:
            self.graph[v] = []

        self.graph[u].append((v, weight))
        self.graph[v].append((u, weight))


def dijkstra(graph, start):

    distances = {node: float('inf') for node in graph.graph}
    distances[start] = 0

    pq = [(0, start)]

    while pq:

        current_distance, current_node = heapq.heappop(pq)

        for neighbor, weight in graph.graph[current_node]:

            distance = current_distance + weight

            if distance < distances[neighbor]:

                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances

def create_city_graph():

    g = Graph()

    g.add_edge("Patient", "Junction1", 2)
    g.add_edge("Junction1", "Metro Hospital", 3)
    g.add_edge("Patient", "Junction2", 4)
    g.add_edge("Junction2", "AIIMS", 5)
    g.add_edge("Junction1", "City Hospital", 6)

    return g


def find_nearest_hospital():

    graph = create_city_graph()

    distances = dijkstra(graph, "Patient")

    hospitals = ["Metro Hospital", "AIIMS", "City Hospital"]

    nearest = min(
        hospitals,
        key=lambda h: distances.get(h, float("inf"))
    )

    return {
        "nearest_hospital": nearest,
        "distance": distances[nearest]
    }