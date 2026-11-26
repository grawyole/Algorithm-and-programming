a = list(map(int, input("Введіть числа через пробіл: ").split()))

pos = 0
neg = 0
zero = 0
for x in a:
    if x > 0:
        pos += 1
    elif x < 0:
        neg += 1
    else:
        zero += 1

print(f"додатних {pos}, від'ємних {neg}, нулів {zero}")