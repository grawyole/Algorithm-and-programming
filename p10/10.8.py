def is_palindrome_iter(s):
    """Перевіряє, чи є рядок s паліндромом; регістр і не-літери ігноруються. Ітеративно."""
    t = "".join(ch.lower() for ch in s if ch.isalpha())
    i, j = 0, len(t) - 1
    while i < j:
        if t[i] != t[j]:
            return False
        i += 1
        j -= 1
    return True


def is_palindrome_rec(s):
    """Перевіряє, чи є рядок s паліндромом; регістр і не-літери ігноруються. Рекурсивно."""
    t = "".join(ch.lower() for ch in s if ch.isalpha())

    def check(x):
        if len(x) <= 1:
            return True
        return x[0] == x[-1] and check(x[1:-1])

    return check(t)


assert is_palindrome_iter("ротатор") == is_palindrome_rec("ротатор") == True
assert is_palindrome_iter("програма") == is_palindrome_rec("програма") == False
assert is_palindrome_iter("") == is_palindrome_rec("") == True