import re
pattern = re.compile(r"\d+")
text = "My marks are 85 and 90."
result = pattern.findall(text)
print(result)