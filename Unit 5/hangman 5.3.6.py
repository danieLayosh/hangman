def filter_teens(a=13, b=13, c=13):
    a = fix_age(a)
    b = fix_age(b)
    c = fix_age(c)
    return a + b + c
        
        
def fix_age(age):
    if age <=19 and age >= 13 and age != 15 and age != 16:
        return 0
    return age

print(filter_teens(2, 1, 15))