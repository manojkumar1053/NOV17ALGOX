def firstDuplicateValue(array):
    char_freq = {}
    for ele in array:
        # char_freq[ele] = char_freq.get(ele, 0) + 1
        if ele in char_freq:
            return ele
        else:
            char_freq[ele] = True
    return -1


# First Unique Character  check first unique chararcter
def groupAnagrams(words):
    anagrams = {}
    for word in words:
        sorted_word = "".join(sorted(word))
        if sorted_word in anagrams:
            anagrams[sorted_word].append(word)
        else:
            anagrams[sorted_word] = [word]
    return list(anagrams.values())


def valid_palindrome(str):
    left = 0
    right = left(str) - 1
    while left < right:
        if str[left] != str[right]:
            return False
        left += 1
        right -= 1
    return True


def balancedBrackets(string):
    open_char = "({["
    close_char = ")}]"

    stack = []

    matching_character = {
        ")": "(",
        "}": "{",
        "]": "["
    }

    for char in string:
        if char in open_char:
            stack.append(char)
        elif char in close_char:
            if len(stack) == 0:
                return False
            if stack[-1] == matching_character[char]:
                stack.pop()
            else:
                return False
    return len(stack) == 0


def serach_insert_position(array, target):
    low, high = 0, len(array) - 1
    while low <= high:
        mid = (low + high) // 2
        mid_val = array[mid]
        if target == mid_val:
            return mid
        elif target > mid_val:
            low = mid + 1
        else:
            high = mid - 1
    return low


# Rotate Image

def rotate_image(matrix):
    print(matrix)
    matrix.reverse()
    for i in range(len(matrix)):
        for j in range(i):
            print(matrix[j])
            matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]
    return matrix


# matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#
# print(rotate_image(matrix1))

def two_sum(array, target):
    nums = {}
    for num in array:
        potential_match = target - num
        if potential_match in nums:
            return [potential_match, num]
        else:
            nums[num] = True
    return nums


def two_sum_2(array, target):
    array.sort()
    left, right = 0, len(array) - 1
    while left < right:
        current_sum = array[left] + array[right]
        if current_sum == target:
            return [array[left], array[right]]
        elif current_sum <= target:
            left += 1
        else:
            right += 1
    return []


def threeNumberSum(array, targetSum):
    # Write your code here.
    array.sort()
    triplets = []
    for i in range(len(array)):
        left, right = i + 1, len(array) - 1
        while left < right:
            current_sum = array[i] + array[left] + array[right]
            if current_sum == targetSum:
                triplets.append([array[i], array[left], array[right]])
                left += 1
                right -= 1
            elif current_sum < targetSum:
                left += 1
            else:
                right -= 1
    return triplets


# Linked List
# Remove nth Node from the end
# BUY and SELL Stocks

def buy_and_sell_stocks(arr):
    min_price = float("inf")
    best = 0
    for price in arr:
        profit = price - min_price

        if profit > best:
            best = profit

        if price < min_price:
            min_price = price

    return best


def buy_sell_2(prices):
    if not prices or len(prices) == 1:
        return 0
    profit = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            profit += prices[i] - prices[i - 1]
    return profit


# Intersection of the two array
def intersect_array(nums1, nums2):
    n1, n2, result = len(nums1), len(nums2), []
    p1 = p2 = 0
    while p1 < len(n1) and p2 < len(n2):
        if n1[p1] < n2[p2]:
            p1 += 1
        elif n1[p1] > n2[p2]:
            p2 += 1
        else:
            result.append(n1[p1])
            p1 += 1
            p2 += 1
    return result


def plus_one(digits):
    for i in reversed(range(len(digits))):
        if digits[i] == 9:
            digits[i] = 0
        else:
            digits[i] += 1
            return digits
        return [1] + digits


# print(plus_one([7, 8, 9]))


# MOVE ELEMENT to the END
def move_zeros(arr):
    i = 0
    for j in range(len(arr)):
        if arr[j] != 0:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    return arr


# print(move_zeros([0, 0, 1, 2, 0, 3, 4, 0]))


def isValidation(board):
    row, col, block = set(), set(), set()
    for i in range(9):
        for j in range(9):
            if board[i][j] != '.':
                r_key = (i, board[i][j])
                c_key = (j, board[i][j])
                b_key = (i // 3, j // 3, board[i][j])
                if (r_key in row) or (c_key in col) or (b_key in block):
                    return False
                row.add(r_key)
                col.add(c_key)
                block.add(b_key)
    return True


def isPalindrome(s):
    str_char = ""
    for char in s:
        if char.isalpha():
            str_char = "".join([str_char, char])
    # str_char.lower()
    return str_char.lower() == str_char.lower()[::-1]


print(isPalindrome("0P"))


def isPalidrome2(str):
    left, right = 0, len(str) - 1

    while left < right:
        while left < right and str[left].isalnum():
            left += 1
        while left < right and str[right].isalnum():
            right -= 1
        if str[left].lower() != str[right].lower():
            return False
        left += 1
        right -= 1
    return True
