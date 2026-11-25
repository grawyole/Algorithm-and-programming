def solve_5_1(a, b, c):
  if a >= b and a >= c:
    return a
  elif b >= a and b >= c:
    return b
  else:
    return c


# Тести:
print(solve_5_1(14, 6, 11))  # Очікується: 14
print(solve_5_1(8, 8, 8))  # Очікується: 8 (межовий випадок рівності)
print(solve_5_1(-4, -9, -2))  # Очікується: -2 (від'ємні числа)
print(solve_5_1(3, 15, 15))  # Очікується: 15 (рівність двох максимальних)