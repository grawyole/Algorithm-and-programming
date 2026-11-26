a = list(map(int, input("Введіть числа через пробіл: ").split()))

old_id = id(a)
i = 0
j = len(a) - 1
while i < j:
    a[i], a[j] = a[j], a[i]
    i += 1
    j -= 1

print(a)
print("той самий список:", id(a) == old_id)