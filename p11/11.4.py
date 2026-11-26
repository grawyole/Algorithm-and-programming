def merge(a, d=1):
    if len(a) <= 1:
        return a, d
    m = len(a) // 2
    left, d1 = merge(a[:m], d + 1)
    right, d2 = merge(a[m:], d + 1)
    out = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            out.append(left[i])
            i += 1
        else:
            out.append(right[j])
            j += 1
    return out + left[i:] + right[j:], max(d1, d2)


A = [5, 2, 9, 1, 5, 6]
res, depth = merge(A)
print("A:", res, "глибина рекурсії:", depth)