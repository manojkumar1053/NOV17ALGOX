# def max_sub_array(k, arr):
#     result = []
#     window_sum, window_start = 0.0, 0
#     for window_end in range(len(arr)):
#         window_sum += arr[window_end]
#
#         if window_end >= k - 1:
#             result.append(window_sum / k)
#             window_sum -= arr[window_start]
#             window_start += 1
#
#     return result
#
#
# def max_sub_array_of_size_k(k, arr):
#     # TODO: Write your cod
#     result = []
#     max_result = float("-inf")
#     window_sum, window_start = 0.0, 0
#     for window_end in range(len(arr)):
#         window_sum += arr[window_end]
#
#         if window_end >= k - 1:
#             result.append(window_sum)
#             window_sum -= arr[window_start]
#             window_start += 1
#
#     return int(max(result))
#

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


def lcp(strs):
    if not strs:
        return ""
    shortest_str = min(strs, key=len)
    for i, char in enumerate(shortest_str):
        for other in strs:
            if other[i] != char:
                return shortest_str[:i]
    return shortest_str


print(lcp(["flower", "flow", "flight"]))


# Sliding Window

def find_avg_subarray(k, array):
    result = []
    window_sum, window_start = 0.0, 0
    for window_end in range(len(array)):
        window_sum += array[window_end]
        if window_end >= k - 1:
            result.append(window_sum / k)
            window_sum -= array[window_start]
            window_start += 1
    return result


# print(find_avg_subarray(5, [1, 3, 2, 6, -1, 4, 1, 8, 2]))

def max_sub_array_of_size_k(k, arr):
    w_sum, w_start = 0, 0
    max_sum = float("-inf")
    for w_end in range(len(arr)):
        w_sum += arr[w_end]
        if w_end >= k - 1:
            max_sum = max(max_sum, w_sum)
            w_sum -= arr[w_start]
            w_start += 1
    return max_sum


# print(max_sub_array_of_size_k(3, [2, 1, 5, 1, 3, 2]))

def smallest_subarray_with_given_sum(s, arr):
    w_sum, w_start = 0.0, 0
    w_min = float("inf")
    for w_end in range(len(arr)):
        w_sum += arr[w_end]
        while w_sum >= s:
            w_min = min(w_min, w_end - w_start + 1)
            w_sum -= arr[w_start]
            w_start += 1
    return 0 if w_min == float("inf") else w_min


# No repeat substring (Longest substring without any repeating character)

def non_repeat_substring(str):
    window_start = 0
    max_length = 0
    char_index_map = {}

    for window_end in range(len(str)):
        right_char = str[window_end]
        if right_char in char_index_map:
            window_start = \
                max(window_start, char_index_map[right_char] + 1)

        char_index_map[right_char] = window_end

        max_length = max(max_length, window_end - window_start + 1)

    return max_length


def longestPalindromicSubstring(string):
    longest = ""
    for i in range(len(string)):
        for j in range(i, len(string)):
            sub_string = string[i:j + 1]
            if len(sub_string) > len(longest) and isPalindrome(sub_string):
                longest = sub_string
    return longest


def isPalindrome(string):
    left_idx, right_idx = 0, len(string) - 1
    while left_idx < right_idx:
        if string[left_idx] != string[right_idx]:
            return False
        left_idx += 1
        right_idx -= 1
    return True


def longestPalindrome(string):
    currentLongest = [0, 1]
    for i in range(1, len(string)):
        odd = getLP(string, i - 1, i + 1)
        even = getLP(string, i - 1, i)
        longest = max(odd, even, key=lambda x: x[1] - x[0])
        currentLongest = max(longest, currentLongest, key=lambda x: x[1] - x[0])
    return string[currentLongest[0]:currentLongest[1]]


def getLP(string, left_idx, right_idx):
    while left_idx >= 0 and right_idx < len(string):
        if string[left_idx] != string[right_idx]:
            break
        left_idx -= 1
        right_idx += 1
    return [left_idx+1, right_idx]
