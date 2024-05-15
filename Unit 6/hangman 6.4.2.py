def longest(my_list):
    longest = 0
    for i in my_list:
        if len(i) > longest:
            longest = len(i)
    return longest