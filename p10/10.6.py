import time


def fib_iter(n):
    """Повертає n-те число Фібоначчі ітеративно (fib(0)=0, fib(1)=1)."""
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def fib_naive(n):
    """Наївна рекурсія для n-го числа Фібоначчі (повільна, лише для порівняння)."""
    if n < 2:
        return n
    return fib_naive(n - 1) + fib_naive(n - 2)


def fib_rec(n, memo=None):
    """Рекурсивне n-те число Фібоначчі з мемоізацією (словник memo)."""
    if memo is None:
        memo = {}
    if n < 2:
        return n
    if n not in memo:
        memo[n] = fib_rec(n - 1, memo) + fib_rec(n - 2, memo)
    return memo[n]


assert fib_iter(0) == fib_rec(0) == 0
assert fib_iter(1) == fib_rec(1) == 1
assert fib_iter(10) == fib_rec(10) == 55
assert fib_iter(30) == fib_rec(30) == 832040

# Порівняння часу для n = 35
t0 = time.perf_counter()
fib_naive(35)
t1 = time.perf_counter()
fib_rec(35)
t2 = time.perf_counter()
print(f"наївний: {t1 - t0:.3f} с, з мемоізацією: {t2 - t1:.6f} с")