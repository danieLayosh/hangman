input_letter = input("Guess a letter:").lower()

if len(input_letter) > 1 and input_letter.isalpha() == False:
    print("E3")
elif len(input_letter) > 1:
    print("E1")
elif input_letter.isalpha() == False:
    print("E2")
else:
    print(input_letter)