import heapq

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, v, u, cost):
        if v not in self.graph:
            self.graph[v] = []
        self.graph[v].append((u, cost))

    def a_star_search(self, start, goal, heuristic):
        open_list = []
        heapq.heappush(open_list, (heuristic[start], 0, start, []))
        closed_set = set()

        while open_list:
            _, cost, node, path = heapq.heappop(open_list)

            if node in closed_set:
                continue

            path = path + [node]
            closed_set.add(node)

            if node == goal:
                return path

            for neighbor, move_cost in self.graph.get(node, []):
                if neighbor not in closed_set:
                    total_cost = cost + move_cost + heuristic[neighbor]
                    heapq.heappush(open_list, (total_cost, cost + move_cost, neighbor, path))

        return None

# Example usage:
g = Graph()
g.add_edge('A', 'B', 1)
g.add_edge('A', 'C', 4)
g.add_edge('B', 'C', 2)  # Fix: 2 should be an integer, not a string
g.add_edge('B', 'D', 5)
g.add_edge('C', 'D', 1)

g_heuristic = {'A': 7, 'B': 6, 'C': 2, 'D': 0}

print("A* search from A to D:")
print(g.a_star_search('A', 'D', g_heuristic))
