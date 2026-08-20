with open("data.bin", "ab+") as file:
    file.write(b"Hello Python\n")

    file.seek(0)
    data = file.read()

    print(data)