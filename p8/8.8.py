a = list(map(int, input("Введіть цілі числа через пробіл: ").split()))
k = int(input("Введіть кількість позицій зсуву k: "))

for _ in range(k):
    first = a.pop(0)
    a.append(first)

print(a)