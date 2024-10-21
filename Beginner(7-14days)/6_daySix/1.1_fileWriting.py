#list of tasks 
tasks = ["Buy groceries", "Walk the dog", "Read a book"]

path = r"C:/Users/lucian/Desktop/python/Beginner(7-14days)/daySix/tasks.txt"

#open a file in write mode
with open(path, "w") as file:
    for task in tasks:
        file.write(task + "\n") #write each task in new line
print(f"File saved at : {path}")