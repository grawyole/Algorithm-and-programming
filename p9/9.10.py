m, k = map(int, input("Введіть розміри першої матриці m k: ").split())
a = []
for i in range(m):
    a.append(list(map(int, input(f"Перша матриця, рядок {i + 1}: ").split())))

k2, n = map(int, input("Введіть розміри другої матриці k n: ").split())
if k != k2:
    print("помилка: розміри несумісні")
else:
    b = []
    for i in range(k2):
        b.append(list(map(int, input(f"Друга матриця, рядок {i + 1}: ").split())))

    res = [[0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            for t in range(k):
                res[i][j] += a[i][t] * b[t][j]

    for i in range(m):
        for j in range(n):
            print(f"{res[i][j]:4d}", end="")
        print()