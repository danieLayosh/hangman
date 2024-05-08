def func(num1, num2):
    """This function takes two numbers as input and returns their sum.
    :param num1: num1 value
    :param num2: num2 value
    :type num1: int
    :type num2: int
    :return: sum of num1 and num2
    :rtype: int
    """
    return num1 + num2

def main():
    print(func(2, 3))
    help(func)
    
if __name__ == "__main__":
    main()