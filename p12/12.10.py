"""Data types: sorted strings as lists of characters.
Two words are anagrams if their sorted letters are equal.
Sorting takes O(n log n).
"""

pairs = [("кіт", "тік"), ("кіт", "кит")]

for s1, s2 in pairs:
    print(s1, s2, "anagram:", sorted(s1) == sorted(s2))