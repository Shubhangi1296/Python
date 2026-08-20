with open("demo.txt", "w+") as file:
    file.write("Hello Python\n")
    file.write("This is w+ mode\n")
    file.write("We can write and read")

    file.seek(0)

    print("File content:")
    print(file.read())

print("Operation completed")