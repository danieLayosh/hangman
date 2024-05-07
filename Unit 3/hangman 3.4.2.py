user_input = input("Enter a string: ")
first_char = user_input[0]
modified_string = first_char + user_input[1:].replace(first_char, 'e')
print(modified_string)