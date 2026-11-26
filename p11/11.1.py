def selection(a):
    a = a[:]
    cmp = swp = 0
    for i in range(len(a) - 1):
        m = i
        for j in range(i + 1, len(a)):
            cmp += 1
            if a[j] < a[m]:
                m = j
        if m != i:
            a[i], a[m] = a[m], a[i]
            swp += 1
    return a, cmp, swp


A = [5, 2, 9, 1, 5, 6]
B = [1, 2, 3, 4, 5]
C = [5, 4, 3, 2, 1]
D = []
E = [7]

for name, data in [("A", A), ("B", B), ("C", C), ("D", D), ("E", E)]:
    res, cmp, swp = selection(data)
    print(name, "порівнянь:", cmp, "обмінів:", swp)