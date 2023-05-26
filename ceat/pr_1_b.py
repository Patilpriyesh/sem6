class Graph:
    def __init__(self):
        self.graph = {
            "A": ["B", "C"],
            "B": ["D", "E"],
            "C": ["F"],
            "D": [],
            "E": ["F"],
            "F": [],
        }
        self.visited = []

    def dfs(self, node):
        if node not in self.visited:
            print(node, end=" ")
            self.visited.append(node)
            for neighbour in self.graph[node]:
                self.dfs(neighbour)

grp = Graph()
grp.dfs("A")