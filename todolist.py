# To Do List

todo_list=[]

def add_list():
    item = input("Enter a new Task:")
    todo_list.append(item)
    print(f"{item} added to the list")
def display_list():
    print("***************")
    print("To Do List App")
    print("***************")
    for index,item in enumerate(todo_list,start=1):
        print(f"{index} - {item}")
def update_list():
    pass
def remove_list():
    display_list()
    index = int(input("Enter the item number:"))
    if 0<= index <len(todo_list):
        removed_item = todo_list.pop(index-1)
        print(f"{removed_item} removed from the list")
    else:
        print("Invalid input!!!")
while True:
    print("---------------")
    print("To Do List App")
    print("---------------")
    print("1 - Add To List")
    print("2 - Display List")
    print("3 - Update List")
    print("4 - Remove From List")
    print("5 - Exit")

    option = input("Enter your option:")

    if option == '1':
        add_list()
    elif option == '2':
        display_list()
    elif option == '3':
        update_list()
    elif option == '4':
        remove_list()
    elif option == '5':
        print("Exit")
        break
    else:
        print("Invalid Option")
    