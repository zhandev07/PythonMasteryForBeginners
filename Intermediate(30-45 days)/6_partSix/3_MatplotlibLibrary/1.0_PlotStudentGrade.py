import matplotlib.pyplot as plt

# Sample data
students = ["Alice", "Bob", "Cindy", "David"]
grades = [85, 90, 75, 92]

# Create a bar plot
plt.bar(students, grades)
plt.xlabel("Students")
plt.ylabel("Grades")
plt.title("Student Grades")
plt.show()
