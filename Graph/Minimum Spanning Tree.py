from queue import PriorityQueue


class MST:
    def __init__(self, n, arr):
        self.adj = arr
        self.total = 0
        self.visited = [False for i in range(n)]
        self.pq = PriorityQueue()

    def insert_adjacent_of(self, u):
        for item in self.adj[u]:
            val, vertex = item[0], item[1]
            if not self.visited[vertex]:
                self.pq.put((val, vertex))

    def mst(self, source):
        self.visited[source] = True
        self.insert_adjacent_of(source)
        while not self.pq.empty():
            front = self.pq.get()
            val, vertex = front[0], front[1]
            if not self.visited[vertex]:
                self.total += val
                self.visited[vertex] = True
                self.insert_adjacent_of(vertex)
        return self.total


if __name__ == '__main__':
    x = input().split()
    """
    node = # vertices
    edge = # edge
    """
    node, edge = int(x[0]), int(x[1])
    print(node, edge)

    """
    adj = Adjacency List
    """
    adj = [[] for i in range(node)]
    for i in range(edge):
        x = input().split()
        """
        edge description: u v edge_value
        """
        adj[int(x[0])].append((int(x[2]), int(x[1])))

    source = 0
    print(MST(node, adj).mst(source))

    
