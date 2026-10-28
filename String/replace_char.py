# Replace all occurrences of a given character with another character. 
str = input("Enter a string: ")
char = input("Enter the character to be replaced: ")
new_char = input("Enter the new character: ")
result = str.replace(char, new_char)
print("String after replacing characters:", result)