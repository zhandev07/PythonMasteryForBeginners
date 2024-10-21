#write a csv file 
import csv
import os

#specify the path where csv to be saved 
path = r"C:/Users/lucian/Desktop/python/Beginner(7-14days)/6_daySix/date.csv"

#ensure the dirctory exist before write the file
os.makedirs(os.path.dirname(path), exist_ok=True)

#wite a csv file now to specifile path

with open(path, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age", "Country"])
    writer.writerow(["python", 8, "Tanzania"])
    writer.writerow(["php", 16, "Kenya"])
    writer.writerow(["java", 29, "Uganda"])

print(f"File saved at: {path}")