def reverse_number_iter(n):
    """Повертає число з цифрами n у зворотному порядку (n >= 0), ітеративно."""
    rev = 0
    while n > 0:
        rev = rev * 10 + n % 10
        n //= 10
    return rev


def _reverse_helper(n, acc):
    """Допоміжна функція з акумулятором для reverse_number_rec."""
    if n == 0:
        return acc
    return _reverse_helper(n // 10, acc * 10 + n % 10)


def reverse_number_rec(n):
    """Повертає число з цифрами n у зворотному порядку (n >= 0), рекурсивно."""
    return _reverse_helper(n, 0)


assert reverse_number_iter(12345) == reverse_number_rec(12345) == 54321
assert reverse_number_iter(7) == reverse_number_rec(7) == 7
assert reverse_number_iter(1200) == reverse_number_rec(1200) == 21