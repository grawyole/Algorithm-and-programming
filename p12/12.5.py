"""Data types: sets for subset and disjointness checks.
Both checks take O(n) on average for input sizes n.
"""

x = [1, 5]
y = [1, 5, 7, 9, 11]

print("subset:", set(x) <= set(y))
print("disjoint:", set(x).isdisjoint(set(y)))