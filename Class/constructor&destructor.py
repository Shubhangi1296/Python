class Student:
    def __init__(self, name, age, course):
        self.name = name 
        self.age = age 
        self.course = course 

    def display(self):
        print("Student Details")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Course:", self.course)

    def __del__(self):
        print("Student object destroyed:", self.name)

s1 = Student("Shubhangi", 20, "CSE")
s2 = Student("Rohit", 21, "IT")

s1.display()
s2.display()

del s1
del s2

print("End of the program")