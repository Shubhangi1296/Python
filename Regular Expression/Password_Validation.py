import re
password = input("Enter password: ")
pattern = re.compile(r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&]).{8,}$")
if pattern.match(password):
    print("Valid Password")
else:
    print("Invalid Password")