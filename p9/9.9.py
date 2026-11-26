n = int(input("Введіть розмір квадратної матриці n: "))
a = []
for i in range(n):
    a.append(list(map(int, input(f"Введіть рядок {i + 1}: ").split())))

res = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        res[i][j] = a[n - 1 - j][i]

for i in range(n):
    for j in range(n):
        print(f"{res[i][j]:4d}", end="")
    print()