def is_greater(my_list, n):
    result = [item for item in my_list if item > n]
    return result

result = is_greater([1, 30, 25, 60, 27, 28], 28)
print(result)