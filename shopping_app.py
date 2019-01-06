# Create a new empty list named shopping_list

shopping_list = []



# Create a function named add_list that declares a parametr named item
    # Add the item to the list
def add_list(items):
    shopping_list.append(items)
    # Notify user that the item was added, and state the number of items in the list current
    print("Added! List has {} items.".format(len(shopping_list)))


def show_help():
    print("What should we pick up at the store? ")
    print("""
Enter 'DONE' to stop adding items.
Enter 'HELP' for this help.
    """)
show_help()
while True:
    new_items = input("> ")

    if new_items == 'DONE':
        break
    elif new_items == 'HELP':
        show_help()
        continue

    # Call add to list with new_item as an argument
    add_list(new_items)
