import nltk 
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('punkt_tab')

text = "Python is a powerful programming language."

words = word_tokenize(text)

print("Original Text:", text)
print("Word Tokens:", words)
