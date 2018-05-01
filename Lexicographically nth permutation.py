# Algo's described clearly on the following link
# https://math.stackexchange.com/questions/60742/finding-the-n-th-lexicographic-permutation-of-a-string


def nth_permutation(alpha, n):
    # alpha is the list of item, and
    # n is the nth permutation, that is to be found out
    perm = []
    t = len(alpha)
    fact = [1 for i in range(t)]
    for i in range(2, t):
        fact[i] = fact[i-1]*i

    for i in range(t-1, 0, -1):
        if n % fact[i]:
            p = int(n // fact[i])
            perm.append(alpha[p])
            n %= fact[i]
            del alpha[p]
        else:
            p = int((n // fact[i]) - 1)
            n -= (p * fact[i])
            perm.append(alpha[p])
            del alpha[p]

    perm.append(alpha[0])
    del alpha[:]
    return perm


if __name__ == '__main__':
    alpha = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print('I/P:', alpha)
    ans = nth_permutation(alpha, 1000000)
    print('O/P:', ans)

