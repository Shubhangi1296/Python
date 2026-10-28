from array import * 

# Creating an array 
arr = array('i', [10, 20, 30, 40, 50])
print("Original Array:")
for i in arr:
    print(i, end=" ")

# Append element 
arr.append(60)
print("\n\nAfter Append:")
for i in arr:
    print(i, end=" ")

# Insert element 
arr.insert(2, 25)
print("\n\nAfter Insert:")
for i in arr:
    print(i, end=" ")

# Remove element
arr.remove(40)
print("\n\nAfter Remove:")
for i in arr:
    print(i, end=" ")

# Search element
x = int(input("\n\nEnter element to search: "))
if x in arr:
    print("Element found at index", arr.index(x))
else:
    print("Element not found")

# Update element 
position = int(input("\nEnter index to update: "))
value = int(input("Enter new value: "))
arr[position] = value 
print("\nAfter Update:")
for i in arr:
    print(i, end=" ")

# Display Length 
print("\n\nLength of array =", len(arr))

# Traverse array 
print("Traversing Array:")
for i in range(len(arr)):
    print("arr[", i, "] =", arr[i])