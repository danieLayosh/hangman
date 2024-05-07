user_input = input("Please enter a string: ")

midpoint = len(user_input) // 2

first_half = user_input[:midpoint]
second_half = user_input[midpoint:]

modified_string = first_half.lower() + second_half.upper()

print(modified_string)