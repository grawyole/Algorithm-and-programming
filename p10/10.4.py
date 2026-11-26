def power_iter(a, n):
    """Обчислює a^n для n >= 0 без **, за O(log n) (двійкове піднесення)."""
    res = 1
    base = a
    while n > 0:
        if n % 2 == 1:
            res *= base
        base *= base
        n //= 2
    return res


def power_rec(a, n):
    """Обчислює a^n для n >= 0 без **, рекурсивно, за O(log n)."""
    if n == 0:
        return 1
    half = power_rec(a, n // 2)
    if n % 2 == 0:
        return half * half
    return half * half * a


assert power_iter(2, 10) == power_rec(2, 10) == 1024
assert power_iter(5, 0) == power_rec(5, 0) == 1
assert power_iter(3, 4) == power_rec(3, 4) == 81