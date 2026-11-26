def linear(a, x):
    for i, v in enumerate(a):
        if v == x:
            return i, i + 1
    return -1, len(a)


A = [5, 2, 9, 1, 5, 6]
print(linear(A, 9))
print(linear(A, 100))