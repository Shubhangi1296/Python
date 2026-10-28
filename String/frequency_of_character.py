# Find the number of times a specified character appears in a string. 
str = input("Enter a string : ")
char = input("Enter a character to find its frequency : ")
count = 0
for ch in str:
    if ch == char:
        count += 1
print("Frequency of", char, "is:", count)
