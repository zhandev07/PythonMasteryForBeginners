path = r"C:/Users/lucian/Desktop/python/Beginner(7-14days)/daySix/tasks.txt"

def display_tasks():
    with open(path, "r") as file:
        tasks = file.readlines()
        print("\n Your To-Do List:")
        for task in tasks:
            print(task.strip())

def add_task():
    task = input("Enter a new task: ")

    with open(path, "w") as file:
        file.write(task + "\n")
    print(f"Task '{task}' added")

#main prgram loop
while True:
    print('\n1 View tasks: ')
    print("2. Add task")
    print("3. Exit")
    choice = input("choose an option: ")

    if choice == "1":
        display_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        print("goodbye!")
        break
    else:
        print("Invalid choice. Pleae try again")