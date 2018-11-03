"""
Watch this video to get more clear
https://www.youtube.com/watch?v=GiN3jRdgxU4
"""

from queue import Queue
import math


class MaxFlow:
    parent = None

    def __init__(self, node, graph):
        """
        :param node: # of nodes in the graph
        :param graph: the original graph as adjacency matrix form

        self.parent : keeps records of an augmented path
        """
        self.node = node
        self.graph = graph
        self.parent = None

    def bfs(self, src, sink):
        """
        :param src: source node
        :param sink: destination node
        :return: if there is a path from src to sink

        This method stores the augmented path in 'self.parent'
        """

        self.parent = {}

        visited = [False]*self.node
        q = Queue()
        q.put(src)
        visited[src] = True

        while not q.empty():
            u = q.get()

            if u == sink:
                break

            for index, val in enumerate(self.graph[u]):
                if val > 0 and not visited[index]:
                    q.put(index)
                    visited[index] = True
                    self.parent[index] = u

        return True if visited[sink] else False

    def edmonds_karp(self, src, sink):
        max_flow = 0

        while self.bfs(src, sink):
            """
            Checks if there is any path from 'src' to 'sink'
            """

            path_flow = math.inf

            """
            Find the edge with smallest 
            value in the augmented path
            """
            s = sink
            while s != src:
                path_flow = min(path_flow,
                                self.graph[self.parent[s]][s])
                s = self.parent[s]
            max_flow += path_flow

            """
            Reduces smallest edge value from forward edges, and
            add smallest edge value to backward edges
            """
            v = sink
            while v != src:
                u = self.parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = self.parent[v]

            self.parent = None

        return max_flow


if __name__ == '__main__':
    graph = [
        [0, 16, 13, 0, 0, 0],
        [0, 0, 10, 12, 0, 0],
        [0, 4, 0, 0, 14, 0],
        [0, 0, 9, 0, 0, 20],
        [0, 0, 0, 7, 0, 4],
        [0, 0, 0, 0, 0, 0]
    ]

    # graph = [
    #     [0, 3, 0, 3, 0, 0, 0],
    #     [0, 0, 4, 0, 0, 0, 0],
    #     [3, 0, 0, 1, 2, 0, 0],
    #     [0, 0, 0, 0, 2, 6, 0],
    #     [0, 1, 0, 0, 0, 0, 1],
    #     [0, 0, 0, 0, 0, 0, 9],
    #     [0, 0, 0, 0, 0, 0, 0]
    # ]

    m = MaxFlow(6, graph)
    print('Max Flow:', m.edmonds_karp(0, 5))

