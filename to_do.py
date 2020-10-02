class ToDo:
    def __init__(self):
        self.items = []

    def add(self, entry):
        # append the added entry to the current list
        self.items.append(entry)
        return print("Item is added successfully.")

    def get(self):
        # verify if current list is empty
        if not self.items:
            return print("The list is currently empty.")
        # display the current list if not empty
        else:
            for entry in range(len(self.items)):
                print(entry + 1, ".", self.items[entry])
            return self.items

    def delete(self, index):
        try:
            self.items.pop(index)
        except IndexError:
            return -1


todo = ToDo()

while True:
    print("""~#--------------#~  MENU  ~#--------------#~
Select an option:
    Enter \"1\" to add an item
    Enter \"2\" to view the complete items
    Enter \"3\" to update an item
    Enter \"4\" to delete the item
    Enter \"5\" to exit
    """)

    try:
        user_input = int(input(">>>: "))
        if user_input == 1:
            print("------- ADD AN ITEM -------")
            item = input(">>> Add: ")
            todo.add(item)

        elif user_input == 2:
            print("------- TO DO LISTS -------")
            items = todo.get()

        elif user_input == 3:
            print("------- UPDATE AN ITEM -------")
            items = todo.get()
            try:
                item = int(input(">>> Enter the item number to modify: "))
                if item == 0 or item > len(items):
                    print("Invalid item number. Please try again.")
                else:
                    # update the item in the list
                    new_item = input(">>> New value: ")
                    items[item - 1] = new_item
                    print("Item is modified successfully.")
            except ValueError as e:
                print('Error type: ', type(e), "is occurring. Please try again.")

        elif user_input == 4:
            print("------- REMOVE AN ITEM -------")
            items = todo.get()
            try:
                item = int(input(">>> Enter the item number to remove: "))
                if item == 0:
                    print("Invalid item number. Please try again.")
                else:
                    # remove the item in the list
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
