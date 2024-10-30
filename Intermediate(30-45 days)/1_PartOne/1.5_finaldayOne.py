# Morning Routine as OOP
class Person:
    def __init__(self, name):
        self.name = name

    def wake_up(self):
        return f"{self.name} wakes up."
    
    def eat_breakfast(self):
        return f"{self.name} eats breakfast"
    
# A subclass for a specific type of person: Student
class Student(Person):
    def study(self):
        return f"{self.name} is studying"

# A subclass for another type of person: Worker
class Worker(Person):
    def work(self):
        return f"{self.name} is working"
    
#Create an objects for student
student = Student("Python")
print(student.wake_up())
print(student.eat_breakfast())
print(student.study())

#Create an objects for worker
work = Worker("Toni")
print(work.wake_up())
print(work.eat_breakfast())
print(work.work())