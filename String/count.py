# Count the number of vowels, consonants, digits, spaces, and special characters in a given string.
str = input("Enter a string: ")
vowels = 0
consonants = 0
digits = 0
spaces = 0
special_characters = 0
for ch in str:
    if ch.isalpha():
        if ch in 'aeiouAEIOU':
            vowels += 1
        else:
            consonants += 1
    elif ch.isdigit():
        digits += 1
    elif ch.isspace():
        spaces += 1
    else:
        special_characters += 1

print("Count of Vowels: ",vowels)
print("Count of Consonants: ",consonants)
print("Count of Digits: ",digits)
print("Count of Spaces: ",spaces)
print("Count of Special Characters: ",special_characters)
