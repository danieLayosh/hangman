def extend_list_x(list_x, list_y):
    for element in reversed(list_y):
        list_x.insert(0, element)
    return list_x


def main():
    print(extend_list_x([4, 5, 6], [1, 2, 3]))
    
if __name__ == "__main__":
    main()