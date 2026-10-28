with open("student.txt", "r") as file:
    data = file.read()

words = data.split()

print("Total number of words:", len(words))