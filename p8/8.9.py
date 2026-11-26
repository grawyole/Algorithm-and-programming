a = list(map(int, input("Введіть цілі числа через пробіл: ").split()))

res = []
for x in a:
    if x not in res:
        res.append(x)

print(res)