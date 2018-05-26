
""" For element [a, b]
= a + b + ab
= a(1+b) + b + 1 - 1
= a(1+b) + (1+b) - 1
= (a + 1) * (b + 1) - 1
= (1+a) * (1 + b) - 1
"""

""" For element [a, b, c]
= a + b + c + ab + bc + ca + abc 
= a + ac + b + bc + ab + abc + c + 1 - 1
= a(1+c) + b(1+c) + ab(1+c) + c + 1 - 1
= (a + b + ab + 1)(1+c) - 1 
= (1+a) * (1+b) * (1+c) - 1 
"""


def product_of_sum(arr):
    n = len(arr)
    ans = 1
    for i in range(n):
        ans *= arr[i]+1

    return ans - 1


if __name__ == '__main__':
    arr = [1, 2, 3, 4]
    print(product_of_sum(arr))

