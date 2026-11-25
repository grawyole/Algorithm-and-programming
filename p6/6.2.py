n = int(input("Введіть натуральне число n: "))
cnt = 0
even = 0

m = n

while m > 0:
    digit = m % 10
    cnt += 1
    if digit % 2 == 0:
        even += 1
    m //= 10

print(f"Кількість цифр = {cnt}, парних = {even}")