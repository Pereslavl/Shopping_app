

shopping_list = []


def show_help():
    print("What should we pick up at the store? ")
    print("""
Enter 'DONE' to stop adding items.
Enter 'HELP' for this help.
Enter 'SHOW' to see your current list.
    """)


def add_list(items):
    shopping_list.append(items)
    print("Added! List has {} items.".format(len(shopping_list)))


def show_list():
    print("Here`s your list:")
    for item in shopping_list:
        print(item)

show_help()
while True:
    new_items = input("> ")
    if new_items == 'DONE':
        break
    elif new_items == 'HELP':
        show_help()
        continue


# Define a function named  show_list that prints all the items in the list
# HINT: Make sure to run itself.
    elif new_items == "SHOW":
        show_list()
        continue

    #Finable the SHOW command to show  the list. Don`t forget to update  the HELP documentation
    add_list(new_items)

show_list()
