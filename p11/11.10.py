import random
import time


def selection(a):
    a = a[:]
    for i in range(len(a) - 1):
        m = i
        for j in range(i + 1, len(a)):
            if a[j] < a[m]:
                m = j
        a[i], a[m] = a[m], a[i]
    return a


def insertion(a):
    a = a[:]
    for i in range(1, len(a)):
        k = i
        while k > 0 and a[k - 1] > a[k]:
            a[k - 1], a[k] = a[k], a[k - 1]
            k -= 1
    return a


def bubble(a):
    a = a[:]
    for i in range(len(a) - 1):
        swapped = False
        for j in range(len(a) - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
        if not swapped:
            break
    return a


def merge(a):
    if len(a) <= 1:
        return a
    m = len(a) // 2
    left, right = merge(a[:m]), merge(a[m:])
    out = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            out.append(left[i])
            i += 1
        else:
            out.append(right[j])
            j += 1
    return out + left[i:] + right[j:]


def quick(a):
    a = a[:]

    def qs(lo, hi):
        if lo >= hi:
            return
        p = a[hi]
        i = lo
        for j in range(lo, hi):
            if a[j] < p:
                a[i], a[j] = a[j], a[i]
                i += 1
        a[i], a[hi] = a[hi], a[i]
        qs(lo, i - 1)
        qs(i + 1, hi)

    qs(0, len(a) - 1)
    return a


data = [random.randint(0, 10000) for _ in range(2000)]
funcs = {
    "вибором": selection,
    "вставками": insertion,
    "бульбашкою": bubble,
    "злиттям": merge,
    "швидке": quick,
    "sorted()": sorted,
}

print(f"{'алгоритм':<12}{'час, с':>10}")
for name, f in funcs.items():
    t0 = time.perf_counter()
    f(data)
    print(f"{name:<12}{time.perf_counter() - t0:>10.4f}")