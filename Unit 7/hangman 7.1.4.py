def squared_numbers(start, stop):
    """
    Returns a list of squared numbers between start and stop (inclusive).

    :param start: The starting integer.
    :type start: int
    :param stop: The stopping integer.
    :type stop: int
    :return: A list of squared numbers from start to stop.
    :rtype: list
    """
    result = []
    current = start
    
    while current <= stop:
        result.append(current ** 2)
        current += 1
    
    return result