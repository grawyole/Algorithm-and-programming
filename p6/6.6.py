n = int(input("Введіть натуральне число n: "))

if n < 2:
    print("ні просте, ні складене")
else:
    prime = True
    i = 2
    while i * i <= n:
        if n % i == 0:
            prime = False
            break
        i += 1
    if prime:
        print("просте")
    else:
        print("складене")