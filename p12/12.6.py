"""Data types: dictionary name -> score.
Building the dictionary and finding max and min take O(n).
"""

students = [("Шевченко", 92), ("Коваль", 74), ("Бондар", 92), ("Ткач", 58)]

scores = {}
for name, score in students:
    scores[name] = score

best = max(scores, key=scores.get)
worst = min(scores, key=scores.get)
print(f"best: {best} ({scores[best]}), worst: {worst} ({scores[worst]})")