class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_student(self):
        print("Name:", self.name)
        print("Age:", self.age)

class Engineering(Student):
    def engineering_info(self):
        print("Branch: CSE")
        print("Subject: Python")

class Management(Student):
    def management_info(self):
        print("Branch: MBA")
        print("Subject: Marketing")

s1 = Engineering("Shubhangi", 20)
s2 = Management("Karan", 21)
s3 = Engineering("Riya", 22)

print("Engineering Student")
s1.display_student()
s1.engineering_info()
s3.display_student()
s3.engineering_info()

print("\nManagement Student")
s2.display_student()
s2.management_info()