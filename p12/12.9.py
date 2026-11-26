"""Data types: dictionaries item -> price, with key set operations.
Set operations on keys take O(n + m) on average.
"""

s1 = {"хліб": 25, "молоко": 30}
s2 = {"хліб": 23, "сир": 90}

common = s1.keys() & s2.keys()
for item in sorted(common):
    print(f"common: {item}, cheapest {min(s1[item], s2[item])}")

print("only in 1:", ", ".join(sorted(s1.keys() - s2.keys())))
print("only in 2:", ", ".join(sorted(s2.keys() - s1.keys())))