n = int(input("Введіть натуральне число n: "))
i = 1
cnt = 0

while i <= n:
    if n % i == 0:
        print(i, end=" ")
        cnt += 1
    i += 1

print(f"({cnt} дільників)")