def quick(a):
    a = a[:]
    cmp = swp = 0

    def qs(lo, hi):
        nonlocal cmp, swp
        if lo >= hi:
            return
        p = a[hi]
        i = lo
        for j in range(lo, hi):
            cmp += 1
            if a[j] < p:
                a[i], a[j] = a[j], a[i]
                swp += 1
                i += 1
        a[i], a[hi] = a[hi], a[i]
        swp += 1
        qs(lo, i - 1)
        qs(i + 1, hi)

    qs(0, len(a) - 1)
    return a, cmp, swp


A = [5, 2, 9, 1, 5, 6]
B = [1, 2, 3, 4, 5]
C = [5, 4, 3, 2, 1]

for name, data in [("A", A), ("B", B), ("C", C)]:
    res, cmp, swp = quick(data)
    print(name, "порівнянь:", cmp, "обмінів:", swp)