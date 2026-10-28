# Write a program to input a string and display its length without using the len() function. 
word = input("Enter a string: ")
count = 0
for ch in word:
    count += 1
print("Length of string is:", count)
