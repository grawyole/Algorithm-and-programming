a = list(map(int, input("Введіть числа через пробіл: ").split()))

even_sum = 0
odd_sum = 0
for i in range(len(a)):
    if i % 2 == 0:
        even_sum += a[i]
    else:
        odd_sum += a[i]

print(f"парні індекси {even_sum}, непарні {odd_sum}")