def insertion(a):
    a = a[:]
    cmp = swp = 0
    for i in range(1, len(a)):
        k = i
        while k > 0:
            cmp += 1
            if a[k - 1] <= a[k]:
                break
            a[k - 1], a[k] = a[k], a[k - 1]
            swp += 1
            k -= 1
    return a, cmp, swp


A = [5, 2, 9, 1, 5, 6]
B = [1, 2, 3, 4, 5]
C = [5, 4, 3, 2, 1]

for name, data in [("A", A), ("B", B), ("C", C)]:
    res, cmp, swp = insertion(data)
    print(name, "порівнянь:", cmp, "обмінів:", swp)