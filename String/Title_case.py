# Convert the first letter of every word to uppercase. 
str = input("Enter a string: ")
words = str.split()
for i in range(len(words)):
    words[i] = words[i].capitalize()
result = " ".join(words)
print("String in title case:", result)