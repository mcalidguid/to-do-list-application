class ToDo:
    def __init__(self):
        self.items = []

    def add(self, entry):
        self.items.append(entry)

    def get(self):
        return self.items

    def delete(self, index):
        try:
            self.items.pop(index)
        except IndexError:
            return -1


todo = ToDo()

while True:
    print("""---------------------
Select an option:
    Enter \"1\" to add an item
    Enter \"2\" to update an item
    Enter \"3\" to view the complete items
    Enter \"4\" to delete the item
    Enter \"5\" to exit
    """)

    try:
        user_input = int(input(">>>: "))
        if user_input == 1:
            print("------- ADD AN ITEM -------")
            item = input(">>> Add: ")
            todo.add(item)
            print("Item is added successfully.")

        elif user_input == 2:
            print("------- UPDATE AN ITEM -------")
            items = todo.get()
            if not items:
                print("The list is currently empty.")
            else:
                try:
                    for item in range(len(items)):
                        print(item + 1, ".", items[item])
                    item = int(input(">>> Enter the item number to modify: "))
                    if item == 0 or item > len(items):
                        print("Invalid item number. Please try again.")
                    else:
                        new_item = input(">>> New value: ")
                        items[item-1] = new_item
                        print("Item is modified successfully.")
                except ValueError as e:
                    print('Error type: ', type(e), "is occurring. Please try again.")

        elif user_input == 3:
            print("------- TO DO LISTS -------")
            items = todo.get()
            if not items:
                print("The list is currently empty.")
            else:
                for item in range(len(items)):
                    print(item+1, ".", items[item])

        elif user_input == 4:
            print("------- REMOVE AN ITEM -------")
            items = todo.get()
            if not items:
                print("The list is currently empty.")
            else:
                try:
                    for item in range(len(items)):
                        print(item + 1, ".", items[item])
                    item = int(input(">>> Enter the item number to remove: "))
                    if item == 0:
                        print("Invalid item number. Please try again.")
                    else:
                        result = todo.delete(item-1)
                        if result == -1:
                            print("Invalid item number. Please try again.")
                        else:
                            print("Item is deleted successfully.")
                except ValueError as e:
                    print('Error type: ', type(e), "is occurring. Please try again.")

        elif user_input == 5:
            print("Danke, tschüss!~")
            break

        else:
            print("Invalid input.")

    except ValueError as e:
        print('Error type: ', type(e), "is occurring. Please try again.")