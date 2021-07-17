# Merge two sorted list

# In place Naive

def merge_test(l1,l2,m,n):

    for i in range(n):
        l1[i+m] = l2[i]
    return l1.sort()


def merged_sorted_array(list1, list2):
    m = len(list1)
    n = len(list2)

    while m > 0 and n > 0:
        if list1[m - 1] > list2[n - 1]:
            list1[m + n - 1] = list2[m - 1]
            m -= 1
        else:
            list1[m + n - 1] = list2[n - 1]
            n -= 1
    while n > 0:
        list1[n - 1] = list2[n - 1]
        n -= 1

