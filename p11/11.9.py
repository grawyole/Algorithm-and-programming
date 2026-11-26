def binary_rec(a, x, lo=0, hi=None):
    if hi is None:
        hi = len(a) - 1
    if lo > hi:
        return -1
    mid = (lo + hi) // 2
    if a[mid] == x:
        return mid
    if a[mid] < x:
        return binary_rec(a, x, mid + 1, hi)
    return binary_rec(a, x, lo, mid - 1)


def binary(a, x):
    lo, hi = 0, len(a) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if a[mid] == x:
            return mid
        if a[mid] < x:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1


S = [1, 3, 5, 7, 9, 11]
assert all(binary(S, x) == binary_rec(S, x) for x in range(13))
print("ітеративний і рекурсивний пошук збігаються")