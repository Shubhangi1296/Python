with open("data.bin", "wb") as file:
    file.write(b"Hello Python\n")
    file.write(b"Welcome to binary file handling\n")
    file.write(b"This is wb mode")

print("Binary data written successfully")