def bubble(a):
    a = a[:]
    cmp = swp = passes = 0
    for i in range(len(a) - 1):
        passes += 1
        swapped = False
        for j in range(len(a) - 1 - i):
            cmp += 1
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swp += 1
                swapped = True
        if not swapped:
            break
    return a, cmp, swp, passes


B = [1, 2, 3, 4, 5]
res, cmp, swp, passes = bubble(B)
print("B проходів:", passes, "порівнянь:", cmp, "обмінів:", swp)