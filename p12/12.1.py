"""Data types: dictionary for character frequency.
Counting takes O(n) with O(1) average dictionary access.
Sorting the k unique characters takes O(k log k).
"""

text = "абракадабра"

counts = {}
for ch in text:
    counts[ch] = counts.get(ch, 0) + 1

top = sorted(counts.items(), key=lambda x: (-x[1], x[0]))[:3]
print(", ".join(f"{ch}:{cnt}" for ch, cnt in top))