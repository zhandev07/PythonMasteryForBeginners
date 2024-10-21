with open("tasks.txt", "r") as file:
    file.seek(10) #move the pointer to the 10th byte
    content = file.read(5) #Read 5 bytes from that point
    print(content)