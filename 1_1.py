import nltk
nltk.download('book')
from nltk.book import text1
long_words_count = sum(1 for word in text1 if len(word) > 10)
print(f"Броят на думите с дължина по-голяма от 10 е: {long_words_count}")
