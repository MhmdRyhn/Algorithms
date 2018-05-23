""" Visit following links to get more clear
http://www.shafaetsplanet.com/?p=1961
https://www.topcoder.com/community/data-science/data-science-tutorials/binary-indexed-trees/

"""


class BIT:
    data = [0]
    tree = None
    sz = None

    def __init__(self, data):
        self.sz = len(data)
        self.data += data[:]
        self.sz = len(self.data)
        self.tree = [0 for i in range(self.sz)]
        self.__create_tree()


    """
    This function creates the initial tree
    """
    def __create_tree(self):
        for i in range(1, self.sz):
            x = i

            while x <= self.sz:
                self.tree[x] += self.data[i]
                x += x & -x


    """
    This function updates the value 
    at a specific position in array
    """
    def update(self, pos, val):
        if pos == 0:
            return None

        while pos <= self.sz:
            self.tree[pos] += val
            pos += pos & -pos


    """
    This function returns sum of value in 1...pos
    """
    def query(self, pos):
        s = 0

        while pos > 0:
            s += self.tree[pos]
            pos -= pos & -pos

        return s




if __name__ == '__main__':
    data = [8, 7, 6, 5, 4, 3, 2, 1]
    bit = BIT(data)
    print('Sum of index 1 to 3:', bit.query(3))
    print('Before adding, Sum of index 1 to 4:', bit.query(4))
    bit.update(3, -6)
    print('After adding, Sum of index 1 to 4:', bit.query(4))
    print('Sum of index 1 to 5:', bit.query(5))

