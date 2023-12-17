from collections import deque

class SearchAlgorithm:
    def __init__(self, graph):
        self.graph = graph
        self.count_parameters = {
            'enqueues': 0,
            'extensions': 0,
            'queue_size': 0,
            'path_elements': 0,
            'path_cost': 0
        }

    def update_count(self, parameter, value):
        if parameter in self.count_parameters:
            self.count_parameters[parameter] += value
            self.graph.update_count_display(self.count_parameters)

    def search(self, start, end):
        pass  # Implement the search algorithm here

class BFS(SearchAlgorithm):
    def search(self, start, end):
        queue = deque([start])
        visited = set([start])

        while queue:
            node = queue.popleft()
            self.graph.highlight_node(node)
            self.update_count('extensions', 1)

            if node == end:
                return True

            for neighbor in self.graph.neighbors(node):
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)
                    self.graph.highlight_edge((node, neighbor))
                    self.update_count('enqueues', 1)

            self.update_count('queue_size', len(queue))

        return False

# ... other algorithms ...

