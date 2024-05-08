str_input = input("Please enter a word: ")
str_input = str_input.lower()

if str_input == str_input[::-1]:
    print("OK")
else:
    print("NOT")