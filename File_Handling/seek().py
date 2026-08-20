with open("demo.txt", "r") as file:
    file.seek(5)
    data = file.read()
    
    print("Data after position 5:")
    print(data)