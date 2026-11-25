def solve_5_2(n):
  if n > 0:
    return "додатне"
  elif n < 0:
    return "від'ємне"
  else:
    return "нуль"

# Тести:
print(solve_5_2(-6))  # Очікується: від'ємне
print(solve_5_2(0))  # Очікується: нуль
print(solve_5_2(25))  # Очікується: додатне
print(solve_5_2(1))  # Очікується: додатне (межовий випадок)