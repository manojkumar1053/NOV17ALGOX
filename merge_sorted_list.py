def merge_sorted_arrays(arrays):
    sorted_list = []
    elements_idxs = [0 for array in arrays]

    while True:
        smallest_items = []
        for array_idx in range(len(arrays)):
            relevant_array = arrays[array_idx]
            elements_idx = elements_idxs[array_idx]
            if elements_idx == len(relevant_array):
                continue
            smallest_items.append({"array_idx": array_idx, "num": relevant_array[elements_idx]})

        if len(smallest_items) == 0:
            break

        next_item = get_min_value(smallest_items)
        sorted_list.append(next_item["num"])
        elements_idxs[next_item["array_idx"]] += 1

    return sorted_list


def get_min_value(items):
    min_value_idx = 0
    for i in range(1, len(items)):
        if items[i]["num"] < items[min_value_idx]["num"]:
            min_value_idx = i
    return items[min_value_idx]


arrays = [
    [-79, -43, -15, 89],
    [-48, 13, 20],
    [-33, -19, -8, 12, 40, 44, 50, 52, 91, 95],
    [-100, -43, -8, 17],
    [-15, 81]
]

print(merge_sorted_arrays(arrays))
