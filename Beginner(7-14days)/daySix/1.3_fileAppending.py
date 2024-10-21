#open the file with appending mode
path = r"C:/Users/lucian/Desktop/python/Beginner(7-14days)/daySix/tasks.txt"

with open(path, "a") as file:
    file.write("Go for a run\n") #add new task