with open("demo.txt", "a+") as file:
    file.write("\nNew data added")
    file.write("\nAnother line added")

    file.seek(0)

    print("Complete file content:")
    print(file.read())

print("Operation completed")