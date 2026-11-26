a = list(map(int, input("Введіть числа через пробіл: ").split()))

s = 0
p = 1
for x in a:
    s += x
    p *= x

n = len(a)
avg = s / n
print(f"сума {s}, добуток {p}, n={n}, середнє {avg:.2f}")