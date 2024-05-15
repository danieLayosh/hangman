def choose_word(file_path, index):
    """
    Chooses a word from a text file at the given index and returns a tuple
    containing the number of unique words and the selected word.

    :param file_path: The path to the text file.
    :type file_path: str
    :param index: The position of the word to select (1-based).
    :type index: int
    :return: A tuple containing the number of unique words and the selected word.
    :retype: tuple
    """
    
    with open(file_path, 'r') as file:
        content = file.read()
    
    words = content.split()
    
    fixed_index = (index - 1) % len(words)
    
    return len(set(words)),  words[fixed_index]

tuple = choose_word(r"Unit 9\words.txt",15)
print(tuple)