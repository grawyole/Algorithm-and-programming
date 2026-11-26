s = input("Введіть рядок: ")

target = input("введіть символ n: ")
if target == "":
    print("символ не введено")
    exit()

indices = [i for i, c in enumerate(s) if c == target]

print(f"{len(indices)} разів, індекси {' '.join(map(str, indices))}")