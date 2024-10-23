import os
import json

__path__ = r"C:/Users/lucian/Desktop/python/Beginner(7-14days)/projects_for_beginers/ToDoListApp/tasks.json"

#function to load tasks  from the file
def load_tasks():
    if os.path.exists(__path__):
        with open(__path__, 'r') as file:
            return json.load(file)
    return[]

#function for save task in json
def save_tasks(tasks):
    with open(__path__, 'w') as file:
            json.dump(tasks, file, indent=4)

#function for display the menu
def tasks_menu():
    print("\nTo-Do List App")
    print("1. add a Task")
    print("2. view All Task")
    print("3. Delete a Task")
    print("4. Mark Task as Complete")
    print("5. Search for a Task")
    print("5. Quit")

#funtion to add new task with descrtpion,due date and priority
def add_task(tasks):
    task_desc = input("Enter a new task: ").strip()
    task_due_date = input("Enter a due date (YYYY-MM-DD): ").strip()
    task_priority = input("Enter Priority (High/Medium/Low): ").strip()

    if task_desc and task_due_date and task_priority in ["high", "medium", "low"]:
        task = {"desc": task_desc, "due_date": task_due_date, "priority": task_priority, "completed": False}
        tasks.append(task)
        save_tasks(tasks)
        print(f"Task Added: {task_desc}, Due by: {task_due_date} and Priority: {task_priority}")
    else:
        print("Invalid input. Please ensure the task, due date, and priority are valid")

#function to display all tasks, with options to filter by proprity
def view_tasks(tasks):
    if not tasks:
       print("Your task list is empty! please add task")
    else:
        print("\nYour Task:")
        for idx, task in enumerate(tasks, start=1):
            status = "☑️ " if task['completed'] else "[ ]"
            print(f"{idx}. {status} {task['desc']} - Due: {task['due_date']} - Priority: {task['priority']}")

# Function to delet task by its number
def delete_task(tasks):
    if not tasks:
         print("No Tasks to delete!")
    else:
        try:
            task_num = int(input("Enter the task number to delete!:"))
            if 1<= task_num <= len(tasks):
                remove_task = tasks.pop(task_num - 1)
                save_tasks(tasks) #update the task again
                print(f" Task removed: {remove_task['desc']}")
            else:
                print("Invalide task number!")
        except ValueError:
            print("Please enter a valid task number!")

# Function to mark a task as complete
def mark_task_complet(tasks):
    if not tasks:
        print("No task to complete!")
    else:
        try:
            task_num = int(input("Enter the task number to mark as complete: "))
            if 1<= task_num <= len(tasks):
                tasks[task_num - 1]["completed"] = True
                save_tasks(tasks)
                print(f"Task {task_num} marked as complete.")
            else:
                print("invalid task number!")
        except ValueError:
            print("Please enter a valid task number")

# Function to search the task by keyworld
def search_task(tasks):
    seach_term = input("Enter a keyword to seach for: ").strip()
    found_tasks = [task for task in tasks if seach_term in task['desc'].lower()]
    if found_tasks:
        print("Serach result:")
        for idx, task in enumerate(found_tasks, start=1):
            status = "☑️ " if task['completed'] else "[ ]"
            print(f"{idx}. {status} {task['desc']} - Due: {task['due_date']} - Priority: {task['priority']} ")   
    else:
        print("No task found matching your search.")


#Main functions to handle the app
def todo_list():
    tasks = load_tasks() 
    while True:
        tasks_menu()
        choice = input("\nEnter you choice: ").strip()

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
           delete_task(tasks)
        elif choice == '4':
           mark_task_complet(tasks)
        elif choice == '5':
           search_task(tasks)
        elif choice == '4':
            print("Goodbye! Thanks and you welcome!")
            break

        else: 
            print("\n Invalid choice, please choose correcty choice!!")


#run the app
todo_list()