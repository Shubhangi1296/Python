import re
# 1. Search for a word
text1 = "Python is easy to learn"
pattern1 = re.compile("Python")
result1 = pattern1.search(text1)
print("1.",result1.group())

# 2. Search for a number
text2 = "My age is 20"
pattern2 = re.compile(r"\d+")
result2 = pattern2.search(text2)
print("2.", result2.group())

# 3. Search for a word starting with P
text3 = "Python is a programming language"
pattern3 = re.compile(r"P\w+")
result3 = pattern3.search(text3)
print("3.", result3.group())

# 4. Search for an email
text4 = "Contact me at student@gmail.com"
pattern4 = re.compile(r"\w+@\w+\.\w+")
result4 = pattern4.search(text4)
print("4.", result4.group())

# 5. Search for a 10-digit mobile number
text5 = "My mobile number is 9876543210"
pattern5 = re.compile(r"\d{10}")
result5 = pattern5.search(text5)
print("5.", result5.group())