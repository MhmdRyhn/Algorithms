""" Visit following links to get more clear
http://www.shafaetsplanet.com/?p=1961
https://www.topcoder.com/community/data-science/data-science-tutorials/binary-indexed-trees/

"""


class BIT:
    __data = [0]
    __tree = None
    __sz = None

    def __init__(self, data):
        self.__sz = len(data)
        self.__data += data
        self.__sz = len(self.__data)
        self.__tree = [0 for i in range(self.__sz + 1)]
        self.__create_tree()


    """
    This function creates the initial tree
    """
    def __create_tree(self):
        for i in range(1, self.__sz):
            x = i

            while x <= self.__sz:
                self.__tree[x] += self.__data[i]
                x += x & -x


    """
    This function adds the value 
    at a specific position in array 
    """
    def update(self, pos, val):
        if pos == 0:
            return None

        while pos <= self.__sz:
            self.__tree[pos] += val
            pos += pos & -pos


    """
    This function returns sum of value in 1...pos
    """
    def query(self, pos):
        s = 0

        while pos > 0:
            s += self.__tree[pos]
            pos -= pos & -pos

        return s




if __name__ == '__main__':
    __data = [8, 7, 6, 5, 4, 3, 2, 1]
    bit = BIT(__data)
    print('Sum of index 1 to 3:', bit.query(3))
    print('Before adding, Sum of index 1 to 4:', bit.query(4))
    bit.update(3, -6)
    print('After adding, Sum of index 1 to 4:', bit.query(4))
    print('Sum of index 1 to 5:', bit.query(5))
