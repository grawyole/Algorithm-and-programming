n = int(input("Введіть натуральне число n: "))
cnt = 0
x = 2

while x <= n:
    prime = True
    d = 2
    while d * d <= x:
        if x % d == 0:
            prime = False
            break
        d += 1
    if prime:
        print(x, end=" ")
        cnt += 1
    x += 1

print()
print(f"({cnt} чисел)")