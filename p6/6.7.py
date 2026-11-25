n = int(input("Введіть натуральне число n: "))

seq = []
total = 0
x, y = 0, 1

for _ in range(n):
    seq.append(str(x))
    total += x
    x, y = y, x + y

print(" ".join(seq) + f", сума = {total}")