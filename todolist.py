def show_menu():
    print("\nTo-Do List Menu")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")

def add_task(tasks):
    task=input("Enter task: ")
    tasks.append([task, False])
    print("Task added.")

def view_tasks(tasks):
    if len(tasks) == 0:
        print("No tasks.")
    else:
        for i in range(len(tasks)):
            status = "Done" if tasks[i][1] else "Pending"
            print(f"{i+1}. {tasks[i][0]} - {status}")

def completed_task(tasks):
    view_tasks(tasks)
    task_num=input("Enter task number to mark as completed: ")
    if task_num.isdigit():
        task_index = int(task_num) - 1
        if 0 <= task_index < len(tasks):
            tasks[task_index][1] = True
            print("Task marked as completed.")
        else:
            print("Invalid task number.")
    else:
        print("Please enter a number.")
    
def delete_task(tasks):
    view_tasks(tasks)
    task_num = input("Enter task number to delete: ")
    if task_num.isdigit():
        task_index = int(task_num) - 1
        if 0 <= task_index < len(tasks):
            tasks.pop(task_index)
            print("Task deleted.")
        else:
            print("Invalid task number.")
    else:
        print("Please enter a number.")

def main():
    tasks = []
    while True:
        show_menu()
        choice = input("Choose an option (1-5): ")
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            completed_task(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            print("Goodbye!")
        else:
            print("Invalid choice.")

main()