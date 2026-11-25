def solve_5_4(x, y):
  if x == 0 and y == 0:
    return "початок"
  elif x == 0:
    return "на осі OY"
  elif y == 0:
    return "на осі OX"
  elif x > 0 and y > 0:
    return "I"
  elif x < 0 and y > 0:
    return "II"
  elif x < 0 and y < 0:
    return "III"
  else:
    return "IV"


# Тести:
print(solve_5_4(5, 2))  # Очікується: I
print(solve_5_4(-3, 6))  # Очікується: II
print(solve_5_4(4, 0))  # Очікується: на осі OX
print(solve_5_4(0, 0))  # Очікується: початок