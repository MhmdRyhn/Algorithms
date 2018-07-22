# Watch the Kadane's Algorithm:
# https://www.youtube.com/watch?v=86CQq3pKSUw


def max_sum_subarray(arr):
    cur_max_sum = arr[0]
    global_max_sum = arr[0]

    sz = len(arr)
    for i in range(1, sz):
        cur_max_sum = max(arr[i], cur_max_sum+arr[i])
        global_max_sum = max(global_max_sum, cur_max_sum)
    return global_max_sum


if __name__ == '__main__':
    arr = [-2, 3, 2, -1]
    ans = max_sum_subarray(arr)
    print(ans)


