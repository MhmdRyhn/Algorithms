# Kadane's Algorithm and the solution:
# https://www.youtube.com/watch?v=86CQq3pKSUw


def max_sum_subarray(arr):
    cur_max_sum = global_max_sum = arr[0]
    start = end = 0

    sz = len(arr)
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
        'global_max_sum': global_max_sum,
        'start': start,
        'end': end
    }
    return ans


if __name__ == '__main__':
    arr = [1, -2, 3, 2, -1, 6, -3]
    ans = max_sum_subarray(arr)
    print('Max Sum of Sub-array:', ans['global_max_sum'])
    print('Start Index of Sub-array:', ans['start'])
    print('End Index of Sub-array:', ans['end'])

