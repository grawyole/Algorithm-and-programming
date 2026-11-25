n = int(input("Введіть натуральне число n: "))
f, s = 1, 0

for i in range(1, n + 1):
    f *= i
    s += f

print(f"{n}! = {f}, сума = {s}")