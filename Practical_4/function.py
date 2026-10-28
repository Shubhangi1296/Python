def list_sum(numbers):
    total = 0 
    for i in numbers:
        total += i
    return total 

def list_average(numbers):
    return sum(numbers) / len(numbers)

def list_max(numbers):
    return max(numbers)

def list_min(numbers):
    return min(numbers)

def count_elements(numbers):
    return len(numbers)

# Main program 
n = int(input("Enter number of elements: "))
list = []
for i in range(n):
    num = int(input("Enter element: "))
    list.append(num)

print("\nList:", list)
print("Sum of elements =", list_sum(list))
print("Average of elements =", list_average(list))
print("Maximum element =", list_max(list))
print("Minimum element =", list_min(list))
print("Number of elements =", count_elements(list))