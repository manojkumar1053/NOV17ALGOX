def threeNumberSort(array, order=None):
    # Write your code here.
    num_freq = {}

    for num in array:
        if num in num_freq:
            num_freq[num] += 1
        else:
            num_freq[num] = 1

    lx = []
    for seq in order:
        if seq in num_freq:
            count = num_freq[seq]
            lx.append([seq] * count)
            # lx.append([seq for seq in range(count)])

    return sum(lx, [])
    #https://www.geeksforgeeks.org/python-ways-to-flatten-a-2d-list/
    # print(lx)
    # ly = []
    # for row in lx:
    #     for value in row:
    #         ly.append(value)
    # #return ly


array = [1, 0, 0, -1, -1, 0, 1, 1]
order = [0, 1, -1]

print(threeNumberSort(array, order))
