def digit_count_iter(n):
    """Повертає кількість цифр натурального n (n >= 0)."""
    if n == 0:
        return 1
    cnt = 0
    while n > 0:
        cnt += 1
        n //= 10
    return cnt


def digit_count_rec(n):
    """Повертає кількість цифр натурального n (n >= 0), рекурсивно."""
    if n < 10:
        return 1
    return 1 + digit_count_rec(n // 10)


assert digit_count_iter(0) == digit_count_rec(0) == 1
assert digit_count_iter(7) == digit_count_rec(7) == 1
assert digit_count_iter(70500) == digit_count_rec(70500) == 5