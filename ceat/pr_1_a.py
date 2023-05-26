class Graph:

    def __init__(self):
        self.graph = {
            "A":["B","C"], 
            "B":["D","E"], 
            "C":["F"], 
            "D":[], 
            "E":["F","I"],
            "F": []
        }
        self.visited = []
        self.queue = []

    def bfs(self, node):
        self.visited.append(node)
        self.queue.append(node)
        
        while self.queue:
            s = self.queue.pop(0)
            print(s, end=" ")
            for neighbour in self.graph:
                if neighbour not in self.visited:
                    self.visited.append(neighbour)
                    self.queue.append(neighbour)


grp = Graph()
grp.bfs("A")