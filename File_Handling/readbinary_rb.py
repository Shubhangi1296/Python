with open("data.bin", "rb") as file:
    data = file.read()

    print("Binary file data:")
    print(data)

print("Binary file read successfully")