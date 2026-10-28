# SGMS Student grade management system

students = []
grades = []

# Add a new student
def add_student():
    name = input("Enter student name: ")
    grade = float(input("Enter grade: "))
    students.append(name)
    grades.append(grade)
    print("Student added successfully")

# Upgrade student grade
def update_grade():
    name = input("Enter student name to update: ")
    if name in students:
        index = students.index(name)
        grades[index] = float(input("Enter new grade: "))
        print("Grade updated successfully")
    else:
        print("Student not found")

# Remove a student
def remove_student():
    name = input("Enter student name to remove: ")
    if name in students:
        index = students.index(name)
        students.pop(index)
        grades.pop(index)
        print("Student removes successfully")
    else:
        print("Student not found")

# Calculate average grade
def average_grade():
    if len(grades) == 0:
        print("No students available")
    else:
        avg = sum(grades) / len(grades)
        print("Average Grade:", avg)

# Display highest and lowest grades
def highest_lowest():
    if len(grades) == 0:
        print("No students available")
    else:
        print("Highest Grade:", max(grades))
        print("Lowest Grade:", min(grades))

# Display all students
def display_students():
    if len(students) == 0:
        print("No students available")
    else:
        print("\nStudent List:")
        for i in range(len(students)):
            print(students[i], ":", grades[i])

# Main Menu
while True:
    print("\nStudent Grade Management System")
    print("1. Add Student")
    print("2. Update Grade")
    print("3. Remove Student")
    print("4. Calculate Average Grade")
    print("5. Display Highest and Lowest Grades")
    print("6. Display Studnet List")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        update_grade()
    elif choice == "3":
        remove_student()
    elif choice == "4":
        average_grade()
    elif choice == "5":
        highest_lowest()
    elif choice == "6":
        display_students()
    elif choice == "7":
        print("Program Ended.")
    else:
        print("Invalid choice.")
    