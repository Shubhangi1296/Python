import re
phone = input("Enter Phone Number: ")
phone_pattern = re.compile(r"^[6-9]\d{9}$")

if phone_pattern.match(phone):
    print("Valid Phone Number")
else:
    print("Invalid Phone Number")