# To-Do List Application (CLI Version)

ToDo_List = []

def show_tasks():
    """Show all tasks in the list"""
    if not ToDo_List:
        print("\nNo tasks available!")
    else:
        print("\nYour To-Do List:")
        for index, task in enumerate(ToDo_List, start=1):
            print(f"{index}. {task}")

def add_task():
    """Add a new task to the list"""
    task = input("\nEnter a new task: ")
    ToDo_List.append(task)
    print(f'Task "{task}" added successfully!')

def remove_task():
    """Remove a task from the list"""
    show_tasks()
    try:
        task_no = int(input("\nEnter task number to remove: ")) - 1
        if 0 <= task_no < len(ToDo_list):
            removed_task = ToDo_List.pop(task_no)
            print(f'Task "{removed_task}" removed successfully!')
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")

def main():
    """Main function to run the To-Do List"""
    while True:
        print("\nTo-Do List Menu:")
        print("1. Show Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            show_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice! Please select a valid option.")

if __name__ == "__main__":
    main()
