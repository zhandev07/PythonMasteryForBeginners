#open the file in read mode
path = r"C:/Users/lucian/Desktop/python/Beginner(7-14days)/daySix/tasks.txt"

with open(path, "r") as file:
    tasks = file.readlines() #read all lines into list
    for task in tasks:
        print(task.strip()) #print each taks without exatra spacing
