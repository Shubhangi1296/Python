# Print all duplicate characters in a string
str =input("Enter a string: ")
duplicates = " "
for ch in str:
    if str.count(ch) > 1 and ch not in duplicates:
        duplicates += ch
print("Duplicate characters in the string :", duplicates)