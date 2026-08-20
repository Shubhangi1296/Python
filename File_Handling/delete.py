import os

if os.path.exists("newfile.txt"):
    os.remove("newfile.txt")
    print("File deleted successfully.")
else:
    print("File does not exist.")