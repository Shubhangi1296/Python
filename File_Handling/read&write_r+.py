file =  open("demo.txt", "r+")

file.write("\nNew data added using r+ mode")
file.write("\nThis mode supports reading and writing")

print("Data written successfully")

file.close()