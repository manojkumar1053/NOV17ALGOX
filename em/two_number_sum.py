def target_sum(sum, array):
    num_dict = {}
    for number in array:
        potential_match = sum - number
        if potential_match in num_dict:
            return True
        else:
            num_dict[number] = True
    return False


print(target_sum(4, [1, 2, 3]))


def target_sum_2(sum, array):
    array.sort()
    left = 0
    right = len(array) - 1

    while left < right:
        current_sum = array[left] + array[right]
        if current_sum == sum:
            return True
        elif current_sum < sum:
            right -= 1
        elif current_sum > sum:
            left += 1

    return True


print(target_sum_2(41, [30, 11, 2, 3]))
