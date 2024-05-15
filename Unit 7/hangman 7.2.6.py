def display_menu():
    print("\nMenu:")
    print("1. Print the shopping list")
    print("2. Print the number of items in the list")
    print("3. Check if an item is in the list")
    print("4. Count occurrences of an item")
    print("5. Remove an item from the list")
    print("6. Add an item to the list")
    print("7. Print all illegal items")
    print("8. Remove duplicates from the list")
    print("9. Exit")

def print_shopping_list(shopping_list):
    print("Shopping list:", shopping_list)

def print_number_of_items(shopping_list):
    print("Number of items in the list:", len(shopping_list))

def check_item_in_list(shopping_list):
    item = input("Enter an item to check: ")
    if item in shopping_list:
        print(f"{item} is in the list.")
    else:
        print(f"{item} is not in the list.")

def count_item_occurrences(shopping_list):
    item = input("Enter an item to count: ")
    count = shopping_list.count(item)
    print(f"{item} appears {count} times in the list.")

def remove_item(shopping_list):
    item = input("Enter an item to remove: ")
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"{item} has been removed from the list.")
    else:
        print(f"{item} is not in the list.")

def add_item(shopping_list):
    item = input("Enter an item to add: ")
    shopping_list.append(item)
    print(f"{item} has been added to the list.")

def print_illegal_items(shopping_list):
    illegal_items = [item for item in shopping_list if len(item) < 3 or not item.isalpha()]
    print("Illegal items in the list:", illegal_items)

def remove_duplicates(shopping_list):
    shopping_list[:] = list(dict.fromkeys(shopping_list))
    print("Duplicates have been removed from the list.")

def main():
    shopping_list = input("Enter your shopping list (comma-separated): ").split(',')
    
    while True:
        display_menu()
        choice = int(input("Enter your choice (1-9): "))
        
        if choice == 1:
            print_shopping_list(shopping_list)
        elif choice == 2:
            print_number_of_items(shopping_list)
        elif choice == 3:
            check_item_in_list(shopping_list)
        elif choice == 4:
            count_item_occurrences(shopping_list)
        elif choice == 5:
            remove_item(shopping_list)
        elif choice == 6:
            add_item(shopping_list)
        elif choice == 7:
            print_illegal_items(shopping_list)
        elif choice == 8:
            remove_duplicates(shopping_list)
        elif choice == 9:
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 9.")

if __name__ == "__main__":
    main()