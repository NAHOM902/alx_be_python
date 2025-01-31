def main():
    shopping_list = []  # Initialize the shopping list as an empty list

    while True:
        display_menu()  # Show the menu to the user
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            # Add an item to the shopping list
            item = input("Enter the item to add: ").strip()
            if item:
                shopping_list.append(item)
                print(f"'{item}' has been added to the shopping list.")
            else:
                print("Invalid input. Item cannot be empty.")
        elif choice == '2':
            # Remove an item from the shopping list
            item = input("Enter the item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' has been removed from the shopping list.")
            else:
                print(f"'{item}' is not in the shopping list.")
        elif choice == '3':
            # Display the shopping list
            if shopping_list:
                print("\nCurrent Shopping List:")
                for i, item in enumerate(shopping_list, start=1):
                    print(f"{i}. {item}")
            else:
                print("The shopping list is currently empty.")
        elif choice == '4':
            # Exit the program
            print("Goodbye!")
            break
        else:
            # Handle invalid menu choices
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
