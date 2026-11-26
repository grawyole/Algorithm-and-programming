"""Data types: set for fast membership checks, list for keeping order.
Both approaches take O(n) on average.
"""

a = [3, 1, 4, 1, 5]

print("set:", set(a))

seen = set()
unique = []
for x in a:
    if x not in seen:
        seen.add(x)
        unique.append(x)
print("order kept:", unique)