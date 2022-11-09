"""
Word Occurrences
Estimate: 25 minutes
Actual:   50 minutes
"""

word_to_count = {}
frequency = 0
text = input("Text: ")
words = text.split()

for word in words:
    frequency = words.count(word)
    word_to_count[word] = frequency

max_length = max(len(word) for word in words)
for word in words:
    print(f"{word:{max_length}}:{word_to_count[word]:{max_length}}")
