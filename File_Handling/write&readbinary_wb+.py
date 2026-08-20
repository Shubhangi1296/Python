with open("data.bin", "wb+") as file:
    file.write(b"Hello Python\n")
    file.write(b"This is wb+ mode\n")
    file.write(b"Binary data can be read and written")

    file.seek(0)

    print("Binary file content:")
    print(file.read())

print("Operation completed")