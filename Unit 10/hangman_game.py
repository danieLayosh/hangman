import os

def opening_screen():
  """
  Displays the opening screen of the Hangman game.
  """
  HANGMAN_ASCII_ART = r"""Welcome to the game Hangman 
  _    _ 
 | |  | |
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |
                     |___/"""
					 
  MAX_TRIES = 6

  print(HANGMAN_ASCII_ART + "\n" + str(MAX_TRIES))

def check_win(secret_word, old_letters_guessed):
  """
  Check if the player has guessed all the letters in the secret word

  :param secret_word: The word the player needs to guess.
  :type secret_word: str
  :param old_letters_guessed: A list containing the letters the player has guessed so far.
  :type old_letters_guessed: list
  :return: True if the player has guessed all the letters in the secret word, otherwise False.
  :retype: bool
  """
  for letter in secret_word:
    if letter not in old_letters_guessed:
      return False
  return True
        
def choose_word(file_path, index):
  """
  Return a word from a text file at the given index.

  :param file_path: The path to the text file.
  :type file_path: str
  :param index: The position of the word to select (1-based).
  :type index: int
  :return: The selected word.
  :retype: str
  """
    
  with open(file_path, 'r') as file:
    content = file.read()
    
  words = content.split()
    
  fixed_index = (index - 1) % len(words)
    
  return words[fixed_index]  

def show_hidden_word(secret_word, old_letters_guessed):
  """
  Returns the secret word with underscores for letters not guessed by the player.

  :param secret_word: The word the player needs to guess.
  :type secret_word: str
  :param old_letters_guessed: A list containing the letters the player has guessed so far.
  :type old_letters_guessed: list
  :return: secret word with underscores for letters not guessed by the player.
  :retype: str
  """

  hidden_word = ""
  for letter in secret_word:
      if letter in old_letters_guessed:
          hidden_word += letter
      else:
          hidden_word += " _ "
          
  return hidden_word

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

def print_hangman(num_of_tries):
  """
  Prints the Hangman ASCII art corresponding to the number of tries.
  
  :param num_of_tries: The number of tries the player has made so far.
  :type num_of_tries: int
  """

  HANGMAN_PHOTOS = {0 : """   x-------x""", 
   1 : """    x-------x
  |
  |
  |
  |
  |""", 
   2 : """    x-------x
  |       |
  |       0
  |
  |
  |""",
   3 : """    x-------x
  |       |
  |       0
  |       |
  |
  |""",
   4 : """    x-------x
  |       |
  |       0
  |      /|\\
  |
  |""",
   5 : """    x-------x
  |       |
  |       0
  |      /|\\
  |      /
  |""",
   6 : """    x-------x
  |       |
  |       0
  |      /|\\
  |      / \\
  |"""}
  
  print(HANGMAN_PHOTOS[num_of_tries])

def game_loop(secret_word, old_letters_guessed, MAX_TRIES, num_of_tries):
  """
  The main game loop that handles the game logic.

  :param secret_word: word the player needs to guess.
  :type secret_word: str
  :param old_letters_guessed: A list of the letters the player has guessed so far.
  :type old_letters_guessed: list
  :param MAX_TRIES: max number of tries.
  :type MAX_TRIES: int
  :param num_of_tries: number of tries the player has made so far.
  :type num_of_tries: int
  """

  while num_of_tries < MAX_TRIES:
    letter = input("\nGuess a letter: ")

    if try_update_letter_guessed(letter, old_letters_guessed): # if the letter is legal
      if letter.lower() not in secret_word: # if the letter is not in the secret word
        print(":(")
        num_of_tries += 1
        print_hangman(num_of_tries) # print the hangman
      
      print(show_hidden_word(secret_word, old_letters_guessed)) # print the hidden word
    else: # if the letter is illegal
      print("letter is illegal\n")
      
    if check_win(secret_word, old_letters_guessed): # if the player has guessed all the letters in the secret word
      print("WIN")
      break
    
  if num_of_tries == MAX_TRIES: # if the player has reached the max number of tries
    print("LOSE")
    print("The word was: " + secret_word)  

def start_game():
  """
  init and start the game
  """
  os.system('cls') # clear the screen

  opening_screen() # print the opening screen

  file_path = input("Enter file path: ")
  word_index = int(input("Enter word index: "))
  print("\nLet's start!\n")
  secret_word = choose_word(file_path, word_index)
  old_letters_guessed = []
  MAX_TRIES = 6
  num_of_tries = 0
  
  print_hangman(num_of_tries)
  print(show_hidden_word(secret_word, old_letters_guessed))
  
  game_loop(secret_word, old_letters_guessed, MAX_TRIES, num_of_tries) # start the game
  
def main():
  """
  The main function of the program.
  """
  start_game()
  
if __name__ == "__main__":
  main()