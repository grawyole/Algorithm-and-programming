def solve_5_6(b):
  # Перевіряємо діапазони від більшого до меншого
  if b >= 90:
    return "A"
  elif b >= 82:
    return "B"
  elif b >= 74:
    return "C"
  elif b >= 64:
    return "D"
  elif b >= 60:
    return "E"
  elif b >= 35:
    return "FX"
  else:
    return "F"


# Тести:
print(solve_5_6(88))  # Очікується: B
print(solve_5_6(64))  # Очікується: D (межовий випадок)
print(solve_5_6(35))  # Очікується: FX (межовий випадок)
print(solve_5_6(34))  # Очікується: F