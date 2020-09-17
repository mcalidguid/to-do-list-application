class ToDo:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

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
        Enter \"2\" to view the complete items
        Enter \"3\" to delete the item""")

    user_input = int(input(">>>: "))

    if user_input == 1:
        item = input(">>> Add item to the list: ")
        todo.add(item)
        print("Item is added successfully")

    elif user_input == 2:
        items = todo.get()
        print("Item List:")
        for item in range(len(items)):
            print(item+1, ".", items[item])

    elif user_input == 3:
        items = todo.get()
        print("Item List:")
        for item in range(len(items)):
            print(item + 1, ".", items[item])
        item = int(input(">>> Enter the item number: "))
        result = todo.delete(item-1)
        if result == -1:
            print("Invalid item number")
        else:
            print("Item is removed from the list")
