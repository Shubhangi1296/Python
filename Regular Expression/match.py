import re

# 1. Match a word
pattern = re.compile(r"Hello")
print(pattern.match("Hello World"))

# 2. Match a number
pattern = re.compile(r"\d+")
print(pattern.match("12345"))

# 3. Match a name
pattern = re.compile(r"[A-Z][a-z]+")
print(pattern.match("Shubhangi"))

# 4. Match a phone number
pattern = re.compile(r"[6-9]\d{9}")
print(pattern.match("9876543210"))

# 5. Match an email
pattern = re.compile(r"\w+@\w+\.\w+")
print(pattern.match("abc@gmail.com"))