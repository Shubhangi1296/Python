# Check whether the entered string is a palindrome. 
str = input("Enter a string: ")
if str == str[::-1]:
    print("The String is a palindrome")
else:
    print("The String is not a palindrome")
