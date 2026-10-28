old_word = input("Enter word to replace: ")
new_word = input("Enter new word: ")

with open("student.txt", "r") as file:
    data = file.read()
    
data = data.replace(old_word, new_word)

with open("student.txt", "w") as file:
    file.write(data)
    
print("Word replaced successfully")