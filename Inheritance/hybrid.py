class Student:
    def student_info(self):
        print("Name: Shubhangi")
        print("Age: 20")

class Course(Student):
    def course_info(self):
        print("Course: CSE")
        print("Year: Third Year")

class Exam(Student):
    def exam_info(self):
        print("Exam: Mid Term")
        print("Date: 9th September")

class Result(Course, Exam):
    def result_info(self):
        print("Result: Pass")
        print("Grade: A")

s = Result()

s.student_info()
s.course_info()
s.exam_info()
s.result_info()