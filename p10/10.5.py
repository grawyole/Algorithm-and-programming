def gcd_iter(a, b):
    """Повертає НСД(a, b) алгоритмом Евкліда, ітеративно."""
    while b != 0:
        a, b = b, a % b
    return a


def gcd_rec(a, b):
    """Повертає НСД(a, b) алгоритмом Евкліда, рекурсивно."""
    if b == 0:
        return a
    return gcd_rec(b, a % b)


assert gcd_iter(48, 18) == gcd_rec(48, 18) == 6
assert gcd_iter(17, 5) == gcd_rec(17, 5) == 1
assert gcd_iter(12, 0) == gcd_rec(12, 0) == 12