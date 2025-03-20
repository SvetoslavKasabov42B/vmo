import nltk
from nltk.corpus import brown
from collections import Counter

nltk.download('brown')

words = brown.words()

words = [word.lower() for word in words if word.isalpha()]

word_freq = Counter(words)

most_common_words = word_freq.most_common(10)

for word, freq in most_common_words:
    print(f"{word}: {freq}")

