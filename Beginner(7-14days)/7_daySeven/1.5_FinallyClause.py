# Finally Clause
try:
    file = open('python.txt', 'r')
    content = file.read()
except FileNotFoundError:
    print("File not foundd!")
finally:
    print("Execute complete.")