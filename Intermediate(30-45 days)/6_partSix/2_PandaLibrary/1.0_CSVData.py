import pandas as pd

# Load a CSV file
grades = pd.read_csv("students_grades.csv")

# Display the first few rows
print(grades.head())

# Calculate average grade
print("Average Grade:", grades["Grade"].mean())

# Filter students who scored above 80
high_scorers = grades[grades["Grade"] > 80]
print("High Scorers:\n", high_scorers)
