def max_sub_array(k, arr):
    result = []
    window_sum, window_start = 0.0, 0
    for window_end in range(len(arr)):
        window_sum += arr[window_end]

        if window_end >= k - 1:
            result.append(window_sum / k)
            window_sum -= arr[window_start]
            window_start += 1

    return result


def max_sub_array_of_size_k(k, arr):
    # TODO: Write your cod
    result = []
    max_result = float("-inf")
    window_sum, window_start = 0.0, 0
    for window_end in range(len(arr)):
        window_sum += arr[window_end]

        if window_end >= k - 1:
            result.append(window_sum)
            window_sum -= arr[window_start]
            window_start += 1

    return int(max(result))


# (3, [2, 1, 5, 1, 3, 2])
# test_array = [2, 1, 5, 1, 3, 2]
# k = 3
# print(max_sub_array_of_size_k(k, test_array))


def max_sub_array_of_size_k2(k, arr):
    # TODO: Write your cod
    window_sum, window_start = 0.0, 0
    max_sum = float("-inf")

    for window_end in range(len(arr)):
        window_sum += arr[window_end]

        if window_end >= k - 1:
            max_sum = max(max_sum, window_sum)
            window_sum -= arr[window_start]
            window_start += 1
    return max_sum


test_array = [2, 1, 5, 1, 3, 2]
k = 3


# print(max_sub_array_of_size_k2(k, test_array))

def revesre_word(str):
    for s in reversed(str):
        print(s)




strx = "hello world"
print(revesre_word(strx))
