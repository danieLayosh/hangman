def numbers_letters_count(my_str):
    digit_count = sum(1 for ch in my_str if ch.isdigit())
    non_digit_count = len(my_str) - digit_count
    return [digit_count, non_digit_count]