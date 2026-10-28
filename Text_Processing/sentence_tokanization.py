import nltk
from nltk.tokenize import sent_tokenize 

nltk.download('punkt')
nltk.download('punkt_tab')

text = "Python is a programming language. It is easy to learn. It is widely used."

sentences = sent_tokenize(text)

print("Original Text:", text)
print("Sentence Tokens:")

for sentence in sentences:
    print(sentence)