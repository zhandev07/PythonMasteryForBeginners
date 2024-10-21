# for large file
# Reading line by line:
with open("largefile.txt", "r") as file:
    for line in file:
        print(line.strip()) # strip() removes extra whitespace

#read in chunks
with open("largefile.txt", "r") as file:
    while True:
        chunk = file.read(1024) #read 1024 bytes at a time
        if not chunk:
            break
        print(chunk)