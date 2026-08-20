with open("data.bin", "wb") as file:
    file.write(b"Hello Python\n")
    file.write(b"This is binary data")

print("Binary data written successfully")