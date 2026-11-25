cm = int(input("Введіть довжину в сантиметрах: "))

m = cm // 100
rest = cm % 100
inch = int(cm // 2.54)

print(f"{m} м {rest} см, {inch} дюймів")