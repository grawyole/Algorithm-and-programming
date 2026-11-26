n, m = map(int, input("Введіть кількість рядків і стовпців: ").split())
a = []
for i in range(n):
    a.append(list(map(int, input(f"Введіть рядок {i + 1}: ").split())))

r1, r2 = map(int, input("Введіть два номери рядків (з 0): ").split())
c1, c2 = map(int, input("Введіть два номери стовпців (з 0): ").split())

a[r1], a[r2] = a[r2], a[r1]
for i in range(n):
    a[i][c1], a[i][c2] = a[i][c2], a[i][c1]

for i in range(n):
    for j in range(m):
        print(f"{a[i][j]:4d}", end="")
    print()