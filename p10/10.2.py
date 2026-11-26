def digit_sum_iter(n):
    """Повертає суму цифр натурального n (n >= 0)."""
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s


def digit_sum_rec(n):
    """Повертає суму цифр натурального n (n >= 0), рекурсивно."""
    if n < 10:
        return n
    return n % 10 + digit_sum_rec(n // 10)


assert digit_sum_iter(0) == digit_sum_rec(0) == 0
assert digit_sum_iter(7) == digit_sum_rec(7) == 7
assert digit_sum_iter(12345) == digit_sum_rec(12345) == 15