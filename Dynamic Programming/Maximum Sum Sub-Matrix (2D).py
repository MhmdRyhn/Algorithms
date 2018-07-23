# This problem is just an extension of Kadane's algorithm
# Watch the solution:
# https://www.youtube.com/watch?v=yCQN096CwWM


def max_sum_subarray_1D(arr, sz):
    cur_max_sum = global_max_sum = arr[0]
    start = end = 0

    for i in range(1, sz):
        cur_max_sum = max(arr[i], cur_max_sum+arr[i])
        if cur_max_sum > global_max_sum:
            global_max_sum = cur_max_sum
            end = i

    g = global_max_sum

    for i in range(end, -1, -1):
        g -= arr[i]
        if not g:
            start = i
            break

    ans = {
        'max': global_max_sum,
        'begin': start,
        'end': end
    }
    return ans


def max_sum_subarray_2D(arr_2d, m, n):
    for i in range(m):
        for j in range(1, n):
            arr_2d[i][j] += arr_2d[i][j-1]

    cur_sum, max_sum = 0, 0
    left, right, top, bottom = 0, 0, 0, 0

    for l in range(n):
        for r in range(l, n):
            arr = []
            for k in range(m):
                if l != 0:
                    arr.append(arr_2d[k][r] - arr_2d[k][l-1])
                else:
                    arr.append(arr_2d[k][r])

            ans = max_sum_subarray_1D(arr, m)
            cur_sum = ans['max']
            if cur_sum > max_sum:
                max_sum = cur_sum
                left, right = l, r
                top, bottom = ans['begin'], ans['end']

    result = {
        'sum_max': max_sum,
        'left': left,
        'right': right,
        'top': top,
        'bottom': bottom
    }
    return result


if __name__ == '__main__':
    arr_2d = [
        [2, 1, -3, -4, 5],
        [0, 6, 3, 4, 1],
        [2, -2, -1, 4, -5],
        [-3, 3, 1, 0, 3]
    ]
    m, n = 4, 5

    ans = max_sum_subarray_2D(arr_2d, m, n)
    print(
        'Max Sum:', ans['sum_max'],
        '\nLeft:', ans['left'],
        '\nRight:', ans['right'],
        '\nTop:', ans['top'],
        '\nBottom:', ans['bottom']
    )


