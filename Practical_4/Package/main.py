from StudentPackage.student import student_details 
from StudentPackage.marks import get_marks 
from StudentPackage.result import calculate_result 

name, roll_number, course = student_details()
m1, m2, m3 = get_marks()
total, percentage, grade = calculate_result(m1, m2, m3) 

print("\nStudent Report Card")
print("Name:", name)
print("Roll Number:", roll_number)
print("Course:", course)
print("Subject 1:", m1)
print("Subject 2:", m2)
print("Subject 3:", m3)
print("Total:", total)
print("Percentage:", percentage)
print("Grade:", grade)