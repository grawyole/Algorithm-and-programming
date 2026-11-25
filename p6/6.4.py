n = int(input("Введіть натуральне число n: "))
rev = 0
m = n

while m > 0:
    rev = rev * 10 + m % 10
    m //= 10

print(f"Число у зворотному порядку = {rev}")