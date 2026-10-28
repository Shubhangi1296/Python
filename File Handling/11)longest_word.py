with open("student.txt", "r") as file:
    data = file.read()
    
words = data.split()
longest = max(words, key=len)

print("Longest word:", longest)
print("Length:", len(longest))