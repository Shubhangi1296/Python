import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

nltk.download('punkt')
nltk.download('punkt_tab')

text = "The students are studying and playing games."

words = word_tokenize(text)

stemmer = PorterStemmer()

stemmed_words = [stemmer.stem(word) for word in words]

print("Original Text:", text)
print("Tokens:", words)
print("Stemmed Words:", stemmed_words)

