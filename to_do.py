class ToDo:
    def __init__(self):
        self.items = []

    def add(self, entry):
        # append the added entry to the current list
        self.items.append(entry)
        print("Item is added successfully.\n")

    def get(self):
        # verify if current list is empty
        if not self.items:
            print("The list is currently empty.\n")
        # display the current list if not empty
        else:
            for entry in range(len(self.items)):
                print(entry + 1, ".", self.items[entry])
            return self.items

    def update(self):
        entry = int(input(">>> Enter the item number to modify: "))
        if entry == 0 or entry > len(self.items):
            print("Invalid item number. Please try again.\n")
        else:
            # update the item in the list
            new_entry = input(">>> New value: ")
            self.items[entry - 1] = new_entry
            print("Item is modified successfully.\n")

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
                todo.update()
            except ValueError as e:
                print('Error type: ', type(e), "is occurring. Please try again.\n")

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
