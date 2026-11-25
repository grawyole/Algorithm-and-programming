n = int(input())

a = n // 100
b = (n // 10) % 10
c = n % 10
sum = a + b + c

print(f"{a} {b} {c}, сума = {sum}")