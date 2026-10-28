import calculator 

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("\nArithmetic Operations")
print("Addition = ", calculator.add(num1, num2))
print("Subtraction = ", calculator.substract(num1, num2))
print("Multiplication = ", calculator.multiply(num1, num2))
print("Division = ", calculator.divide(num1, num2))

num = float(input("\nEnter a number to find square and cube: "))
print("Square = ", calculator.square(num))
print("Cube = ", calculator.cube(num))
