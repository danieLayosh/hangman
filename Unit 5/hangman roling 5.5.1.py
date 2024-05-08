def is_valid_input(letter_guessed):
    """This function takes a letter as input and returns True if the input is valid, otherwise False.
    :param letter_guessed: letter_guessed value
    :type letter_guessed: str
    :return: True if the input is valid, otherwise False
    :rtype: bool"""
    
    if len(letter_guessed) > 1 or letter_guessed.isalpha() == False:
        return False
    
    return True

def main():
    print(is_valid_input("a"))
    print(is_valid_input("A"))
    print(is_valid_input("$"))
    print(is_valid_input("ab"))
    print(is_valid_input("app$"))
    
if __name__ == "__main__":
    main()