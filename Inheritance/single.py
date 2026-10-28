class Student:
    def __init__(self, name, age):
        self.name = name 
        self.age = age 

    def display_student(self):
        print("Name:", self.name)
        print("Age:", self.age)

class College(Student):
    def __init__(self, name, age, college):
        super().__init__(name, age)
        self.college = college

    def display_college(self):
        print("College:", self.college)

s1 = College("Shubhangi", 20, "DYPCET")

s1.display_student()
s1.display_college()