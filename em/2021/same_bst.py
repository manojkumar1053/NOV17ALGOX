def rightSmallerThan(array):
    # Write your code here.
    new_array = []
    for i in range(len(array)):
        count = 0
        for j in range(i + 1, len(array)):

            if array[j] <= array[i]:
                count += 1
        new_array.append(count)
        count = 0
    return new_array


print(rightSmallerThan([8, 5, 11, -1, 3, 4, 2]))
