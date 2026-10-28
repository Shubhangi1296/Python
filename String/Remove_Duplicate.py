# Remove duplicate characters while maintaining the original order. 
str = input("Enter a string: ")
result = ""
for ch in str:
    if ch not in result:
        result += ch
print("String after removing duplicates:", result)