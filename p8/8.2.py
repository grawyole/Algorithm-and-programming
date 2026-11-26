a = list(map(int, input("Введіть цілі числа через пробіл: ").split()))

mx = a[0]
imx = 0
mn = a[0]
imn = 0
for i in range(len(a)):
    if a[i] > mx:
        mx = a[i]
        imx = i
    if a[i] < mn:
        mn = a[i]
        imn = i

print(f"max={mx} (індекс {imx}), min={mn} (індекс {imn})")