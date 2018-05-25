# https://people.cs.uct.ac.za/~ksmith/articles/sliding_window_minimum.html


""" Algorithm:
for each element in array:
    1. remove from deque, all items >= element
    2. append the element to the left of deque
    3. remove all values from deque having
       indices <= index of ith element - window size
"""


from collections import deque


class RMQ:
    dq = None
    data = None

    def __init__(self, arr):
        self.data = arr
        self.dq = deque()
        # self.generate()

    def generate(self, win_sz, rettyp=1):
        self.dq.clear()
        sz = len(self.data)
        val, ind = [], []

        if sz <= win_sz or sz < 2:
            if rettyp == 1:
                return self.data
            else:
                return [i for i in range(sz)]

        for i in range(sz):
            # 1 of above mentioned algorithm
            while self.dq and self.dq[0][0] >= self.data[i]:
                self.dq.popleft()

            # 2 of above mentioned algorithm
            self.dq.appendleft((self.data[i], i))

            # 3 of above mentioned algorithm
            while self.dq and self.dq[-1][1] <= i-win_sz:
                self.dq.pop()
            
            # Top item is the minimum value
            if i >= win_sz-1:
                val.append(self.dq[-1][0])
                ind.append(self.dq[-1][1])

        if rettyp == 1:
            return val
        else:
            return ind
    
    def get_value(self, win_sz):
        return self.generate(win_sz)
    
    def get_index(self, win_sz):
        return self.generate(win_sz, 0)


if __name__ == '__main__':
    arr = [10, 2, 3, 7, 34, 9, 6, 11, 4, 5, 18, 44, 36, 32, 21]
    rmq = RMQ(arr)
    ans = rmq.get_value(4)
    print(*ans)

