import os

# Create Directory
dirname = "MyFolder"

if not os.path.exists(dirname):
    os.mkdir(dirname)
    print("Directory created.")
else:
    print("Directory already exists.")

# Check Directory Exists
if os.path.exists(dirname):
    print("Directory exists.")
else:
    print("Directory does not exist.")

# List Files and Directories
print("\nContents of Current Directory:")
for item in os.listdir("."):
    print(item)

# Rename Directory
new_dirname = "NewFolder"
if os.path.exists(dirname):
    os.rename(dirname, new_dirname)
    print("\nDirectory renamed to", new_dirname)

# Delete Directory
if os.path.exists(new_dirname):
    os.rmdir(new_dirname)
    print("Directory deleted.")