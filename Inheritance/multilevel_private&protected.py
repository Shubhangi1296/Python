class Student:
    def __init__(self):
        self.name = "Shubhangi"    # Public Variable
        self._age = 20             # Protected Variable
        self.__course = "CSE"      # Private Variable   

    def student_info(self):
        print("Name:", self.name)
        print("Age:", self._age)
        print("Course:", self.__course)

class Course(Student):
    def course_info(self):
        print("\nCourse Information")
        print("Name:", self.name)
        print("Age:", self._age)
        # print("Course:", self.__course) 

class College(Course):
    def college_info(self):
        print("\nCOllege Information")
        print("Name:", self.name)
        print("Age:", self._age)

s1 = College()

print("Student Information")
s1.student_info()

s1.course_info()
s1.college_info()