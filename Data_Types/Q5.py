from collections import Counter

text = input("Enter a paragraph: ")

words = text.lower().split()

print("Total number of words:", len(words))

frequency = Counter(words)

print("Word frequency:")
for word, count in frequency.items():
    print(word, ":", count)

print("Top 3 most frequent words:")
for word, count in frequency.most_common(3):
    print(word, ":", count)

vowels = "aeiou"
vowel_count = 0

for ch in text.lower():
    if ch in vowels:
        vowel_count += 1

print("Number of vowels:", vowel_count)