class ToDo:
    def __init__(self):
        self.items = []

    def add(self):
        item = input(">>> Add: ")
        # append the added item to the current list
        self.items.append(item)
        print("Item is added successfully.\n")

    def get(self):
        # verify if current list is empty
        if not self.items:
            print("The list is currently empty.\n")
            return 0
        else:
            # display the current list if not empty
            for item in range(len(self.items)):
                print(item + 1, ".", self.items[item])
            return 1

    def update(self):
        index = int(input(">>> Enter the item number to modify: "))
        if index == 0 or index > len(self.items):
            print("Invalid item number. Please try again.\n")
        else:
            # update the item in the list
            item = input(">>> New value: ")
            self.items[index - 1] = item
            print("Item is modified successfully.\n")

    def delete(self):
        index = int(input(">>> Enter the item number to remove: "))
        if index == 0:
            print("Invalid item number. Please try again.\n")
        else:
            try:
                # remove the item in the list
                self.items.pop(index-1)
                print("Item is deleted successfully.\n")
            except IndexError:
                print("Invalid item number. Please try again.\n")


def message(error):
    print("Error Type:", type(error), "is occurring. Please try again.\n")


todo = ToDo()

while True:
    print("""~#--------------#~  MENU  ~#--------------#~
Select an option:
    Enter \"1\" to add an item
    Enter \"2\" to view the complete list
    Enter \"3\" to update an item
    Enter \"4\" to delete an item
    Enter \"5\" to exit""")

    try:
        user_input = int(input(">>>: "))
        if user_input == 1:
            print("------- ADD AN ITEM -------")
            todo.add()

        elif user_input == 2:
            print("------- TO DO LISTS -------")
            todo.get()
            print()

        elif user_input == 3:
            print("------- UPDATE AN ITEM -------")
            if todo.get() == 1:
                try:
                    todo.update()
                except ValueError as e:
                    message(e)

        elif user_input == 4:
            print("------- REMOVE AN ITEM -------")
            if todo.get() == 1:
                try:
                    todo.delete()
                except ValueError as e:
                    message(e)

        elif user_input == 5:
            print("Danke, tschüss! ^_^")
            break

        else:
            print("Invalid input.\n")

    except ValueError as e:
        message(e)
