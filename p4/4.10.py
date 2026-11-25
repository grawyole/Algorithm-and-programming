s = int(input("Введіть дату в форматі DDMMYY: "))

dd = s[0:2]
mm = s[2:4]
rr = s[4:6]

print(f"{dd}.{mm}.20{rr}")