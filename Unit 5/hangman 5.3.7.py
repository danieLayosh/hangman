def chocolate_maker(small, big, x):
    if big * 5 + small < x:
        return False
    elif x % 5 > small:
        return False
    
    return True

print(chocolate_maker(3, 2, 14))