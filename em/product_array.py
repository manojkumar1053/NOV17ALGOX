def arrayOfProducts(array):

    products = [1 for _ in range(len(array))]
    left_products = [1 for _ in range(len(array))]
    right_products = [1 for _ in range(len(array))]

    left_running_product = 1
    for i in range(len(array)):
        left_products[i] = left_running_product
        left_running_product *= array[i]

    right_running_product = 1
    for i in reversed(range(len(array))):
        right_products[i] = right_running_product
        right_running_product *= array[i]

    for i in range(len(array)):
        products[i] = left_products[i] * right_products[i]

    return products


print(arrayOfProducts([1, 2, 3, 4]))
