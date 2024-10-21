import csv

path = r"C:/Users/lucian/Desktop/python/Beginner(7-14days)/6_daySix/date.csv"

#read a csp file
with open(path, "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)