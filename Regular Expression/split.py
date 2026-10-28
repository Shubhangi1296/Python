import re

# 1. Split by space
pattern = re.compile(r"\s+")
print(pattern.split("Hello World Python"))

# 2. Split by comma
pattern = re.compile(r",")
print(pattern.split("Apple,Banana,Mango"))

# 3. Split by comma or space
pattern = re.compile(r"[, ]+")
print(pattern.split("Apple, Banana Mango"))

# 4. Split by hyphen
pattern = re.compile(r"-")
print(pattern.split("10-20-30-40"))

# 5. Split by comma, semicolon or space
pattern = re.compile(r"[,; ]+")
print(pattern.split("Python,Java;C++ HTML"))