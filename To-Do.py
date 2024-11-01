to_do_list = []
def main():
    while True:
        print("\n--- To-Do App Menu ---")
        print("1. Add Item")
        print("2. Delete Item")
        print("3. Modify Item")
        print("4. View Items")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == '1':
            add_item()
        elif choice == '2':
            delete_item()
        elif choice == '3':
            modify_item()
        elif choice == '4':
            view_items()
        elif choice == '5':
            print("Exiting the app. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def add_item():
    item = input("Enter the item you wish to add: ").strip().lower()
    to_do_list.append(item)
    print(f"'{item}' was added\n")

def delete_item():
    item = input("Enter the item you wish to delete: ").strip().lower()
    if item in to_do_list:
        to_do_list.remove(item)
        print(f"'{item}' has been removed.")
    else:
        print("Item does not exist.")

def modify_item():
    old_item = input("Enter the item you wish to change: ")
    if old_item in to_do_list:
        change = input("Enter the new task: ").strip().lower()
        pos = to_do_list.index(old_item)
        to_do_list[pos] = change
        print(f"'{old_item}' has been changed to '{change}'")
    else:
        print("Task entered does not exist.")

def view_items():
    if to_do_list:
        for i, item in enumerate(to_do_list, 1):
            print(f"Current tasks:\n {i}. '{item.capitalize()}'")
    else:
        print("The list is empty.")


if __name__ == "__main__":
    main()
