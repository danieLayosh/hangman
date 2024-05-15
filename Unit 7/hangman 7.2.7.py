def arrow(my_char, max_length):
    for i in range(max_length):
        print(my_char * (i + 1))
    for i in range(max_length - 1,0,-1):
        print(my_char * i)
        
