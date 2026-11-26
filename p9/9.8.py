n, m = map(int, input("Введіть кількість рядків і стовпців: ").split())
a = []
for i in range(n):
    a.append(list(map(int, input(f"Введіть рядок {i + 1}: ").split())))

a.sort(key=sum)

for i in range(n):
    for j in range(m):
        print(f"{a[i][j]:4d}", end="")
    print()