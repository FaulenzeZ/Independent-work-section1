import string
from collections import Counter

with open('text.txt', 'r', encoding='utf-8') as file:
    text = file.read().lower()

for char in string.punctuation + '—–':
    text = text.replace(char, ' ')

words = [word for word in text.split() if len(word) >= 4]

word_counts = Counter(words)
max_frequency = max(word_counts.values())

frequent_words = [word for word, count in word_counts.items() if count == max_frequency]
best_word = min(frequent_words)

print(f"Чаще всего встречается слово: '{best_word}' (повторов: {max_frequency})")
