import string
from collections import Counter

with open('text.txt', 'r', encoding='utf-8') as file:
    text = file.read()

text = text.lower()

punctuation_to_remove = string.punctuation + '—–'
for char in punctuation_to_remove:
    text = text.replace(char, ' ')

words = text.split()

word_counts = Counter(words)
max_frequency = max(word_counts.values())

frequent_words = []
for word, count in word_counts.items():
    if count == max_frequency:
        frequent_words.append(word)

best_word = min(frequent_words)
count = max_frequency

print(f"Чаще всего встречается слово: '{best_word}' (повторов: {count})")
