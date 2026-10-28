from collections import Counter

text = input("Enter a string: ")

choice = input("Ignore case? (yes/no): ")

if choice.lower() == "yes":
    text = text.lower()

frequency = Counter(text)

sorted_frequency = sorted(
    frequency.items(),
    key=lambda x: x[1],
    reverse=True
)

print("Character frequency:")

for char, count in sorted_frequency:
    if char == " ":
        print("Space :", count)
    else:
        print(char, ":", count)