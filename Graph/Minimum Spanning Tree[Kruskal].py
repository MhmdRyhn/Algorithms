class DisjointSet:
    def __init__(self, element):
        """
        :param element: No. of node in the graph

        self.par: self.par[x] means the representative of x
        self.rank: self.rank[representative] means the no. of node the representative holds
        """
        self.element = element
        self.par = [i for i in range(element)]
        self.rank = [1 for i in range(element)]

    def create_set(self, x):
        """
        This method creates a set with one element
        and sets the element itself as its parent
        """
        self.par[x] = x
        self.rank[x] = 1

    def merge_sets(self, x, y):
        """
        This method merges two sets into one
        """
        # x_root is the representative of x
        x_root = self.find_set(x)
        y_root = self.find_set(y)

        """
        Two element having same representative 
        means that they are in.txt the same set
        """
        if x_root == y_root:
            return False  # No merge happened

        """
        If a representative has more elements than other,
        it becomes the representative of the merged set.
        """
        if self.rank[x_root] >= self.rank[y_root]:
            self.rank[x_root] += self.rank[y_root]
            self.par[y_root] = x_root
            self.rank[y_root] = 0
        else:
            self.rank[y_root] += self.rank[x_root]
            self.par[x_root] = y_root
            self.rank[x_root] = 0

        # if self.rank[x_root] >= self.rank[y_root]:
        #     self.par[y_root] = x_root
        # else:
        #     self.par[x_root] = y_root

        return True  # Merge happened

    def find_set(self, x):
        """
        This method returns the representative.
        Moreover, it compresses the path (depth) into 1
        """
        if self.par[x] != x:
            """
            This statement sets the representative 
            as the parent of elements in a set
            """
            self.par[x] = self.find_set(self.par[x])
        return self.par[x]


class Kruskal(DisjointSet):
    def __init__(self, element, graph):
        self.graph = sorted(graph, key=lambda d: d[2])
        super().__init__(element)

    def mst(self):
        """
        :return: The MST info
        """
        i, e = 0, 0
        result = []

        # No. of edge in MST is (No_of_node-1)
        while e < self.element - 1:
            u, v, w = self.graph[i]
            merge_status = self.merge_sets(u, v)
            if merge_status:
                result.append((u, v, w))
                e += 1
            i += 1

        return result


if __name__ == '__main__':
    # x = input().split()
    # node, edge = int(x[0]), int(x[1])
    # print(node, edge)
    #
    # adj = []
    # for i in range(edge):
    #     x = input().split()
    #
    #     # edge description: (u, v, edge_value)
    #     adj.append((int(x[0]), int(x[1]), int(x[2])))

    node = 4
    adj = [
        (0, 1, 9),
        (0, 2, 6),
        (0, 3, 5),
        (1, 3, 15),
        (2, 3, 4)
    ]

    ans = Kruskal(node, adj).mst()
    print('Edges (with weight) in MST are as follows:')
    for edge in ans:
        print(edge[0], ' -> ', edge[1], ' = ', edge[2])

