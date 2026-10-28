class Student:
    def student_info(self):
        print("Name: Shubhangi")
        print("Age: 20")

class Course:
    def course_info(self):
        print("Course: CSE")
        print("Year: Third Year")

class College(Student, Course):
    def college_info(self):
        print("College: DYPCET")
        print("Location: Kolhapur")

s = College()

s.student_info()
s.course_info()
s.college_info()