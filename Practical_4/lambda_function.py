even_odd = lambda x: "Even" if x % 2 == 0 else "Odd"
square = lambda x: x * x 
cube = lambda x: x * x * x
positive_negative = lambda x: "Positive" if x > 0 else "Negative"
greater = lambda a, b: a if a > b else b 

# Main program

num = int(input("Enter a number: "))

print(num, "is", even_odd(num))
print("Square =", square(num))
print("Cube =", cube(num))
print("Number is", positive_negative(num))

num1 = int(input("\nEnter first number: "))
num2 = int(input("Enter second number: ")) 

print("Greater number =", greater(num1, num2))