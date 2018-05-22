class DisjointSet:
    element = None
    """
    'par' keeps tract of the representative 
    for an element in a set
    """
    par = None
    """
    'rank' of a representative represents
    the number of elements in its set
    """
    rank = None



    """
    This function (Constructor) initializes  
    rank=1 & par[x]=x  to each node
    """
    def __init__(self, element):
        self.element = element
        self.par = [i for i in range(element)]
        self.rank = [1 for i in range(element)]



    """
    This function creates a set with one element 
    and sets the element itself as its parent
    """
    def create_set(self, x):
        self.par[x] = x
        self.rank[x] = 1


    
    """
    This function merges two sets into one
    """
    def merge_sets(self, x, y):
        # x_root is the representative of x
        x_root = self.find_set(x)
        y_root = self.find_set(y)

        """
        Two element having same representative 
        means that they are in the same set
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

        # if self.rank[x_root] > self.rank[y_root]:
        #     self.par[y_root] = x_root
        # else:
        #     self.par[x_root] = y_root
        #
        # if self.rank[x_root] == self.rank[y_root]:
        #     self.rank[y_root] += 1

        return True  # Merge happened



    """
    This function returns the representative.
    Moreover, it compresses the path (depth) into 1
    """
    def find_set(self, x):
        if self.par[x] != x:
            """
            This statement sets the representative 
            as the parent of elements in a set
            """
            self.par[x] = self.find_set(self.par[x])
        return self.par[x]


