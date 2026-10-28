import re

# 1. Find all numbers
text1 = "I have 10 apples and 20 oranges"
pattern1 = re.compile(r"\d+")
print("1.", pattern1.findall(text1))

# 2. Find all words starting with P
text2 = "Python is powerful and popular"
pattern2 = re.compile(r"P\w+")
print("2.", pattern2.findall(text2))

# 3. Find all email addresses
text3 = "Emails: abc@gmail.com, xyz@yahoo.com"
pattern3 = re.compile(r"\w+@\w+\.\w+")
print("3.", pattern3.findall(text3))

# 4. Find all mobile numbers
text4 = "Numbers: 9876543210 and 8765432109"
pattern4 = re.compile(r"\d{10}")
print("4.", pattern4.findall(text4))

# 5. Find all vowels
text5 = "Regular Expression"
pattern5 = re.compile(r"[aeiouAEIOU]")
print("5.", pattern5.findall(text5))