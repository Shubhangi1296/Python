# Reverse the given string without using built-in reverse functions. 
str = input("Enter a string : ")
for i in range(len(str)-1, -1, -1):
    print(str[i], end="")
