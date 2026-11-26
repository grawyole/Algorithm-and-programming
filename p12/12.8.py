"""Data types: dictionary converted to a list of pairs for sorting.
Sorting takes O(n log n).
"""

scores = {"Шевченко": 92, "Коваль": 74, "Бондар": 92, "Ткач": 58}

result = sorted(scores.items(), key=lambda x: (-x[1], x[0]))
print(result)