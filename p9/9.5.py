n = int(input("Введіть розмір квадратної матриці n: "))
a = []
for i in range(n):
    a.append(list(map(int, input(f"Введіть рядок {i + 1}: ").split())))

above = 0
below = 0
for i in range(n):
    for j in range(n):
        if j > i:
            above += a[i][j]
        elif j < i:
            below += a[i][j]

print(f"вище = {above}, нижче = {below}")