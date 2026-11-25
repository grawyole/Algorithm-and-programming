n = int(input("Введіть натуральне число n: "))
m = n

mx = 0
mn = 9

while m > 0:
    digit = m % 10
    if digit > mx:
        mx = digit
    if digit < mn:
        mn = digit
    m //= 10

print(f"max = {mx}, min = {mn}")