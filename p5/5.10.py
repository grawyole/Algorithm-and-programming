def solve_5_10(age, sex):
  # Діти до 18 років мають право незалежно від статі
  if age < 18:
    return "так"
  elif sex == "ж" and age >= 60:
    return "так"
  elif sex == "ч" and age >= 65:
    return "так"
  else:
    return "ні"

# Тести:
print(solve_5_10(15, "ч"))  # Очікується: так
print(solve_5_10(45, "ж"))  # Очікується: ні
print(solve_5_10(60, "ж"))  # Очікується: так (межовий випадок)
print(solve_5_10(64, "ч"))  # Очікується: ні (межовий випадок)