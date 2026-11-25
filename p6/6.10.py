n = int(input("Введіть натуральне число n: "))
s, i = 0, 1

while i < n:
    if n % i == 0:
        s += i
    i += 1

if s == n:
    print("досконале")
else:
    print("не досконале")