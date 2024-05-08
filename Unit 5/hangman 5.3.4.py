def last_early(my_str):
    last = my_str[-1]
    if my_str.find(last) < len(my_str) - 1:
        return True
    else: 
        return False

print(last_early("best of luck"))