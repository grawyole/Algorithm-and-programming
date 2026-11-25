n = int(input("Введіть двоцифрове число: "))

a = n // 10
b = n % 10
rev = b * 10 + a
total = n + rev

print(f"{rev}, сума = {total}")