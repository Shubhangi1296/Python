import string

def normalize(text):
    result = ""

    for ch in text.lower():
        if ch.isalnum():
            result += ch

    return result

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

str1 = normalize(str1)
str2 = normalize(str2)

if sorted(str1) == sorted(str2):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")