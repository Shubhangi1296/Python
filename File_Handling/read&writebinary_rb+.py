with open("data.bin", "rb+") as file:
    print("Existing binary data:")
    print(file.read())

    file.write(b"\nNew binary data")
    file.write(b"\nData added using rb+ mode")

print("Binary read and write completed")