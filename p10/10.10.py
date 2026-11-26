def binary_iter(n):
    """Повертає двійкове подання натурального n як рядок (n >= 0), ітеративно."""
    if n == 0:
        return "0"
    bits = ""
    while n > 0:
        bits = str(n % 2) + bits
        n //= 2
    return bits


def binary_rec(n):
    """Повертає двійкове подання натурального n як рядок (n >= 0), рекурсивно."""
    if n < 2:
        return str(n)
    return binary_rec(n // 2) + str(n % 2)


assert binary_iter(0) == binary_rec(0) == "0"
assert binary_iter(1) == binary_rec(1) == "1"
assert binary_iter(10) == binary_rec(10) == "1010"
assert binary_iter(255) == binary_rec(255) == "11111111"