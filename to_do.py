class ToDo:
    def __init__(self):
        self.items = []

    def add(self, entry):
        self.items.append(entry)

    # def update(self, item):
    # 	self.items.replace(item)

    def get(self):
        return self.items

    def delete(self, index):
        try:
            self.items.pop(index)
        except:
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

    user_input = int(input(">>>: "))

    if user_input == 1:
        print("------- ADD AN ITEM -------")
        item = input(">>> Add: ")
        todo.add(item)
        print("Item is added successfully.")

    elif user_input == 2:
        print("------- UPDATE AN ITEM -------")
        #items = todo.get()
        print(">>>: Item List:")    # to be removed
        #for item in range(len(items)):
        #    print(item + 1, ".", items[item])
        #item = int(input(">>>: Enter the item number: "))
        #result = todo.delete(item-1)
        #if result == -1:
        #    print(">>>: Invalid item number. Please try again")
        #else:
        #    print(">>>: Item is updated successfully")

    elif user_input == 3:
        print("------- TO DO LISTS -------")
        items = todo.get()
        for item in range(len(items)):
            print(item+1, ".", items[item])

    elif user_input == 4:
        print("------- REMOVE AN ITEM -------")
        items = todo.get()
        for item in range(len(items)):
            print(item + 1, ".", items[item])
        item = int(input(">>> Enter the item number: "))
        result = todo.delete(item-1)
        if result == 0:
            print("Invalid item number. Please try again.")
        else:
            print("Item is deleted successfully.")

    elif user_input == 5:
        print("Danke, tschüss!~")
        break

    else:
        print("Invalid input.")
