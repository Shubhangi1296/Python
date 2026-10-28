import re

email = input("Enter Email: ")
email_pattern = re.compile(r"^[\w.-]+@[\w.-]+\.\w+$")

if email_pattern.match(email):
    print("Valid Email")
else:
    print("Invalid Email")
    
