n, m = map(int, input("Введіть кількість рядків і стовпців: ").split())
a = []
for i in range(n):
    a.append(list(map(int, input(f"Введіть рядок {i + 1}: ").split())))

s = 0
mx = a[0][0]
mx_r = 0
mx_c = 0
mn = a[0][0]
mn_r = 0
mn_c = 0
for i in range(n):
    for j in range(m):
        s += a[i][j]
        if a[i][j] > mx:
            mx = a[i][j]
            mx_r = i
            mx_c = j
        if a[i][j] < mn:
            mn = a[i][j]
            mn_r = i
            mn_c = j

print(f"max={mx} ({mx_r},{mx_c}), min={mn} ({mn_r},{mn_c}), сума={s}")