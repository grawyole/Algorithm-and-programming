n = int(input("Введіть розмір квадратної матриці n: "))
a = []
for i in range(n):
    a.append(list(map(int, input(f"Введіть рядок {i + 1}: ").split())))

main_sum = 0
side_sum = 0
for i in range(n):
    main_sum += a[i][i]
    side_sum += a[i][n - 1 - i]

print(f"головна = {main_sum}, побічна = {side_sum}")