def binary(a, x):
    lo, hi, mids = 0, len(a) - 1, []
    while lo <= hi:
        mid = (lo + hi) // 2
        mids.append(mid)
        if a[mid] == x:
            return mid, mids
        if a[mid] < x:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1, mids


idx, mids = binary([1, 3, 5, 7, 9, 11], 9)
print("mid:", mids, "індекс:", idx)