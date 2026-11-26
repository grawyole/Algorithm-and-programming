def insertion_key(a, key=lambda x: x, rev=False):
    a = a[:]
    for i in range(1, len(a)):
        cur, k = a[i], i - 1
        while k >= 0 and ((key(a[k]) < key(cur)) if rev else (key(a[k]) > key(cur))):
            a[k + 1] = a[k]
            k -= 1
        a[k + 1] = cur
    return a


print(insertion_key([-5, 2, -1, 3], key=abs))
print(insertion_key([1, 3, 2], rev=True))