def factorial_iter(n):
    """Обчислює n! ітеративно. n >= 0. Повертає ціле число."""
    res = 1
    for i in range(2, n + 1):
        res *= i
    return res


def factorial_rec(n):
    """Обчислює n! рекурсивно. n >= 0. Повертає ціле число."""
    if n <= 1:
        return 1
    return n * factorial_rec(n - 1)


assert factorial_iter(0) == factorial_rec(0) == 1
assert factorial_iter(5) == factorial_rec(5) == 120
assert factorial_iter(10) == factorial_rec(10) == 3628800