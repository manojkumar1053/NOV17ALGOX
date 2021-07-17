def pair_with_targetsum(arr, target_sum):
    # TODO: Write your code here
    return [-1, -1]


def do_target_sum(arr, target_sum):
    pass


freqDict = {}


def buildFreqTable(aList):
    freqDict = {}
    for num in aList:
        if num in freqDict:
            freqDict[num] += 1
        else:
            freqDict[num] = 1

    print(freqDict)


# # return -1
# array = [2, 1, 5, 3, 3, 2, 4]
# print(buildFreqTable(array))


def firstDuplicateValue(arr):
    # Write your code here.
    num_freq = {}
    for num in arr:
        if num in num_freq:
            return num
        else:
            num_freq[num] = True


# arr = [2, 1, 5, 3, 3, 2, 4]
#
# print(firstDuplicateValue(arr))


def remove_duplicates(arr):
    # index of the next non-duplicate element
    next_non_duplicate = 1

    i = 1
    while i < len(arr):
        if arr[next_non_duplicate - 1] != arr[i]:
            arr[next_non_duplicate] = arr[i]
            next_non_duplicate += 1
        i += 1

    return next_non_duplicate


#
# def main():
#     print(remove_duplicates([2, 3, 3, 3, 6, 9, 9]))
#     print(remove_duplicates([2, 2, 2, 11]))
#
#
# main()

def search_triplets(arr):
    triplets = []
    # TODO: Write your code here
    target = 0
    arr.sort()
    for i in range(len(arr) - 2):
        left, right = i + 1, len(arr) - 1
        while left < right:
            current_sum = arr[i] + arr[left] + arr[right]
            if current_sum == target:
                triplets.append([arr[i], arr[left], arr[right]])
                left += 1
                right -= 1
            elif current_sum < target:
                left += 1
            elif current_sum > target:
                right -= 1
    return triplets


# print(search_triplets([-3, 0, 1, 2, -1, 1, -2]))
def reverseWordsInString(string):

