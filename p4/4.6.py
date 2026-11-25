k = int(input("введіть суму в копійках: "))
grn = k // 100
kop = k % 100

print(f"{grn} грн {kop:02d} коп")