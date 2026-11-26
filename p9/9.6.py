n, m = map(int, input("Введіть кількість рядків і стовпців: ").split())
a = []
for i in range(n):
    a.append(list(map(int, input(f"Введіть рядок {i + 1}: ").split())))

pos = 0
neg = 0
zero = 0
for i in range(n):
    for j in range(m):
        if a[i][j] > 0:
            pos += 1
        elif a[i][j] < 0:
            neg += 1
        else:
            zero += 1

print(f"додатних {pos}, від'ємних {neg}, нулів {zero}")