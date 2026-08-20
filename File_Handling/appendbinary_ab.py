with open("data.bin", "ab") as file:
    file.write(b"\nNew binary data")
    file.write(b"\nAnother binary line")
    file.write(b"\nThis is append binary mode")

print("Binary data appended successfully")