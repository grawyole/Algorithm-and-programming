n, m = map(int, input("Введіть кількість рядків і стовпців: ").split())
a = []
for i in range(n):
    a.append(list(map(int, input(f"Введіть рядок {i + 1}: ").split())))

row_sums = []
for i in range(n):
    s = 0
    for j in range(m):
        s += a[i][j]
    row_sums.append(s)

col_sums = []
for j in range(m):
    s = 0
    for i in range(n):
        s += a[i][j]
    col_sums.append(s)

print("рядки:", " ".join(map(str, row_sums)))
print("стовпці:", " ".join(map(str, col_sums)))