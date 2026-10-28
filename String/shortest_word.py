# Find the shortest word in a sentence. 
str = input("Enter a string: ")
words = str.split()
shortest = words[0]
for word in words:
    if len(word) < len(words):
        shortest = word
print("Smallest word in a sentence is : ",shortest)