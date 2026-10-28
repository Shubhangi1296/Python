with open("student.txt", "r") as file:
    data = file.read()
    
words = data.split()
word_count = {}

for word in words:
    word = word.lower()
    
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
        
print(word_count)