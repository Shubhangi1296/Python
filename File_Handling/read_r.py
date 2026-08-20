file = open("demo.txt", "r")

print("File opened in read mode")
data = file.read()
print("File content:")
print(data)

file.close()