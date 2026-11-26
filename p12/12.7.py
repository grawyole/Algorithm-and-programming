"""Data types: dictionary grade -> list of names.
A list is needed because several students can share one grade.
Grouping takes O(n).
"""

students = [("Шевченко", 92), ("Коваль", 74), ("Бондар", 92), ("Ткач", 58)]


def ects(score):
    if score >= 90:
        return "A"
    elif score >= 82:
        return "B"
    elif score >= 74:
        return "C"
    elif score >= 64:
        return "D"
    elif score >= 60:
        return "E"
    elif score >= 35:
        return "FX"
    else:
        return "F"


groups = {}
for name, score in students:
    groups.setdefault(ects(score), []).append(name)

print(groups)