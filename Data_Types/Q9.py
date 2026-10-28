attendance = {
    "Monday": {"Amit", "Rahul", "Priya"},
    "Tuesday": {"Amit", "Priya", "Sneha"},
    "Wednesday": {"Amit", "Priya"},
    "Thursday": {"Amit", "Rahul"},
    "Friday": {"Amit", "Priya"}
}

# Students who attended all classes
all_days = set.intersection(*attendance.values())

# All unique students
all_students = set.union(*attendance.values())

# Students who attended only one class
count = {}

for students in attendance.values():
    for student in students:
        count[student] = count.get(student, 0) + 1

only_one = {student for student in count if count[student] == 1}

print("Students who attended all classes:", all_days)
print("Students who attended only one class:", only_one)
print("Total unique students:", len(all_students))