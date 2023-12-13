import networkx as nx
import matplotlib.pyplot as plt

class Graph:
    def __init__(self):
        self.nodes = nx.Graph()

    def add_node(self, node):
        self.nodes.add_node(node)

    def add_edge(self, node1, node2):
        self.nodes.add_edge(node1, node2)

    def get_neighbors(self, node):
        return list(self.nodes.neighbors(node))

    def get_all_nodes(self):
        return list(self.nodes.nodes())

    def dfs(self, start, end):
        visited = set()
        path = []
        self._dfs_util(start, end, visited, path)

        if not path:
            print("Path not found")
        else:
            print("Path:", " -> ".join(str(path)))

    def _dfs_util(self, node, end, visited, path):
        visited.add(node)
        path.append(node)

        if node == end:
            return True

        for neighbor in self.nodes.neighbors(node):
            if neighbor not in visited:
                if self._dfs_util(neighbor, end, visited, path):
                    return True

        path.pop()
        return False

    def bfs(self, start, end):
        visited = set()
        queue = [(start, [])]

        while queue:
            node, path = queue.pop(0)

            if node not in visited:
                visited.add(node)
                path.append(node)

                if node == end:
                    print("Path:", " -> ".join(str(path)))
                    return

                for neighbor in self.nodes.neighbors(node):
                    if neighbor not in visited:
                        queue.append((neighbor, list(path)))

        print("Path not found")

    def visualize(self):
        nx.draw(self.nodes, with_labels=True, node_color='lightblue', edge_color='gray', font_weight='bold')
        plt.show()

if __name__ == '__main__':
    # Создание нового графа
    graph = Graph()

    # Добавление вершин в граф
    graph.add_node(1)
    graph.add_node(2)
    graph.add_node(3)
    graph.add_node(4)
    graph.add_node(5)
    graph.add_node(6)
    graph.add_node(7)
    graph.add_node(8)
    graph.add_node(9)
    graph.add_node(10)
    graph.add_node(11)
    graph.add_node(12)
    graph.add_node(13)
    graph.add_node(14)
    graph.add_node(15)

    # Добавление ребер в граф
    graph.add_edge(1,3)
    graph.add_edge(2,5)
    graph.add_edge(2,11)
    graph.add_edge(3,2)
    graph.add_edge(3,4)
    graph.add_edge(4,5)
    graph.add_edge(4,6)
    graph.add_edge(5,7)
    graph.add_edge(6,7)
    graph.add_edge(7,8)
    graph.add_edge(7,9)
    graph.add_edge(8,10)
    graph.add_edge(9,10)
    graph.add_edge(9,13)
    graph.add_edge(10,14)
    graph.add_edge(11,12)
    graph.add_edge(11,15)
    graph.add_edge(12,13)
    graph.add_edge(13,14)

    # Инициализация метода поиска в глубину
    print("DFS:")
    graph.dfs(1,9)

    # Инициализация метода поиска в ширину
    print("BFS:")
    graph.bfs(1,9)

    # Визуализация графа
    graph.visualize()

    # Создание нового графа
    graph2 = Graph()

    # Добавление вершин в граф
    graph2.add_node(1)
    graph2.add_node(2)
    graph2.add_node(3)
    graph2.add_node(4)
    graph2.add_node(5)
    graph2.add_node(6)
    graph2.add_node(7)
    graph2.add_node(8)
    graph2.add_node(9)
    graph2.add_node(10)

    # Добавление ребер в граф
    graph2.add_edge(1, 3)
    graph2.add_edge(2, 5)
    graph2.add_edge(2, 7)
    graph2.add_edge(3, 2)
    graph2.add_edge(3, 4)
    graph2.add_edge(4, 5)
    graph2.add_edge(4, 6)
    graph2.add_edge(5, 7)
    graph2.add_edge(6, 7)
    graph2.add_edge(7, 8)
    graph2.add_edge(8, 9)
    graph2.add_edge(9, 10)
    graph2.add_edge(10, 1)

    # Инициализация метода поиска в глубину
    print("DFS:")
    graph2.dfs(1, 6)

    # Инициализация метода поиска в ширину
    print("BFS:")
    graph2.bfs(1, 6)

    # Визуализация графа
    graph2.visualize()