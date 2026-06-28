tasks = []
def show_tasks():
    index = 1
    for task in tasks:
        print(f"{index}. {task}\n")
        index = index + 1
while True:
    print("=== Welcome to the Daily To-Do List Program ===\n--- Main Menu ---\n1. View Tasks\n2. Add a New Task\n3. Delete a Task\n4. Exit Program\n------------------\n")
    choice = input("Please choose an option (1-4): \n")
    if choice == "1":
        if len(tasks) == 0:
            print("Your To-Do list is empty!\n")
        else:
            print("Your Daily Tasks:\n")
            show_tasks()
    elif choice == "2":
        new_task = input("Enter the task you want to add: \n")
        if new_task in tasks:
            print("You have already added this task!\n")
        else:
            tasks.append(new_task)
            print(f"Your new task has been added successfully!\n")
    elif choice == "3":
        if len(tasks) == 0:
            print("Your To-Do list is empty!\n")
        else:
         try:
            print('The remaining tasks:\n')
            show_tasks()
            nb_of_task = int(input("Select the task number to delete: \n"))
            if nb_of_task < 1 or nb_of_task > len(tasks):
                print("Invalid value!\n")
            else:
                del tasks[nb_of_task - 1]
                print("Your task has been deleted successfully!\n")
         except ValueError:
            print("Invalid input\n")
    elif choice == "4":
        print("Thank you ! The program has been closed successfully. Goodbye!\n")
        break
    else:
        continue
