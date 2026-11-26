"""Data types: dictionary for word frequency.
Counting takes O(n) for n words in the text.
"""

text = "алгоритм це послідовність дій алгоритм має бути скінченним"

counts = {}
for w in text.split():
    counts[w] = counts.get(w, 0) + 1

for w, cnt in counts.items():
    if cnt > 1:
        print(w, cnt)