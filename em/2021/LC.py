def numberToWords(num):
    """
    :type num: int
    :rtype: str
    """

    n2w = {1e9: "Billion", 1e6: "Million", 1e3: "Thousand", 1e2: "Hundred",
           90: "Ninety", 80: "Eighty", 70: "Seventy",
           60: "Sixty", 50: "Fifty", 40: "Forty",
           30: "Thirty", 20: "Twenty", 19: "Nineteen",
           18: "Eighteen", 17: "Seventeen", 16: "Sixteen",
           15: "Fifteen", 14: "Fourteen", 13: "Thirteen",
           12: "Twelve", 11: "Eleven", 10: "Ten",
           9: "Nine", 8: "Eight", 7: "Seven",
           6: "Six", 5: "Five", 4: "Four", 3: "Three",
           2: "Two", 1: "One", 0: "Zero"}

    keys = [1000000000, 1000000, 1000, 100, 90, 80, 70,
            60, 50, 40, 30, 20, 19, 18, 17, 16, 15, 14, 13, 12,
            11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

    def dp(n):
        if n <= 20: return n2w[n]
        for div in keys:
            d, r = divmod(n, div)
            if not d:
                continue
            s1 = dp(d) + " " if div >= 100 else ""
            s2 = " " + dp(r) if r else ""
            return s1 + n2w[div] + s2

    return dp(num)


# print(numberToWords(123))


# def fizzBuzz(n):
#     result = []
#     for i in range(1, n + 1):
#         if (i % 3 == 0) and (i % 5 == 0):
#             result.append("FizzBuzz")
#         elif (i % 5 == 0) and (i % 3 != 0):
#             result.append("Buzz")
#         elif (i % 3 == 0) and (i % 5 != 0):
#             result.append("Fizz")
#         else:
#             result.append(str(i))
#     return result

def fizzBuzz(n):
    result = []
    for i in range(1, n + 1):
        if (i % 3 == 0) and (i % 5 == 0):
            result.append("FizzBuzz")
        elif (i % 5 == 0) and (i % 3 != 0):
            result.append("Buzz")
        elif (i % 3 == 0) and (i % 5 != 0):
            result.append("Fizz")
        else:
            result.append(str(i))
    return result


print(fizzBuzz(15))


def fizzBuzz2(n):
    return ["Fizz" * (not i % 3) + "Buzz" * (not i % 5) or str(i) for i in range(1, n + 1)]


print(fizzBuzz2(15))


# Prime_Number_Count

def count_prime(n):
    if n <= 2:
        return 0
    numbers = set()

    for i in range(2, int(n ** 0.5) + 1):
        if i not in numbers:
            for j in range(i * i, n, i):
                numbers.add(j)
    return n - len(numbers) - 2

print(count_prime(20))


def remove_duplicate(arr):
    for idx in range(len(arr)-1,0,-1):
        if arr[idx] == arr[idx-1]:
            arr.pop(idx)
    return len(arr)
