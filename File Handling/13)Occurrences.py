word = input("Enter word to search: ")

count = 0
line_numbers = []

with open("student.txt", "r") as file:
    for line_number, line in enumerate(file, 1):
        words = line.split()
        
        for w in words:
            if w.lower() == word.lower():
                count += 1
                line_numbers.append(line_number)
                
print("Occurrences:", count)
print("Line numbers:", line_number)