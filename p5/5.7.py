def solve_5_7(m):
  if m in (12, 1, 2):
    return "зима"
  elif m in (3, 4, 5):
    return "весна"
  elif m in (6, 7, 8):
    return "літо"
  elif m in (9, 10, 11):
    return "осінь"
  else:
    return "помилка"


# Тести:
print(solve_5_7(7))  # Очікується: літо
print(solve_5_7(10))  # Очікується: осінь
print(solve_5_7(12))  # Очікується: зима
print(solve_5_7(0))  # Очікується: помилка