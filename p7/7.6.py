s = "абракадабра"
target =  "a"

indices = [i for i, c in enumerate(s) if c == target]

print(f"{len(indices)} разів, індекси {' '.join(map(str, indices))}")