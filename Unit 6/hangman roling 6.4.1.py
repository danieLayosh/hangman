def check_valid_input(letter_guessed, old_letters_guessed):
    """
    this function takes a letter as input and returns True if the input is valid and has not been guessed before, otherwise False.

    :param letter_guessed: The character input from the player.
    :type letter_guessed: str
    :param old_letters_guessed: A list containing the letters the player has guessed so far.
    :type old_letters_guessed: list
    :return: True if the input is valid and has not been guessed before, otherwise False.
    :retype: bool
    """
    if len(letter_guessed) != 1 or not letter_guessed.isalpha():
        return False
    
    if letter_guessed.lower() in [letter.lower() for letter in old_letters_guessed]:
        return False
    
    return True

def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """
    attempts to add a newly guessed letter to the list of previously guessed letters.

    :param letter_guessed: The character input from the player.
    :type letter_guessed: str
    :param old_letters_guessed: A list containing the letters the player has guessed so far.
    :type old_letters_guessed: list
    :return: True if the letter was successfully added, otherwise False.
    :retype: bool
    """
    if check_valid_input(letter_guessed, old_letters_guessed):
        old_letters_guessed.append(letter_guessed.lower())
        return True
    else:
        print("X")
        sorted_guessed = sorted([letter.lower() for letter in old_letters_guessed])
        print(" -> ".join(sorted_guessed))
        return False

