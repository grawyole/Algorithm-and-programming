def list_sum_iter(a):
    """Повертає суму елементів списку a, ітеративно (без sum())."""
    total = 0
    for x in a:
        total += x
    return total


def list_sum_rec(a):
    """Повертає суму елементів списку a, рекурсивно: перший елемент плюс сума решти."""
    if not a:
        return 0
    return a[0] + list_sum_rec(a[1:])


assert list_sum_iter([]) == list_sum_rec([]) == 0
assert list_sum_iter([5]) == list_sum_rec([5]) == 5
assert list_sum_iter([1, 2, 3, 4]) == list_sum_rec([1, 2, 3, 4]) == 10