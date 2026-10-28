class Student:
    def student_info(self):
        print("Name: Shubhangi")
        print("Age: 20")

class Course(Student):
    def course_info(self):
        print("Course: Computer Science")
        print("Semester: 5th")

class College(Course):
    def college_info(self):
        print("College: DYPCET")
        print("City: Kolhapur")

s = College()

s.student_info()
s.course_info()
s.college_info()