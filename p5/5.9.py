def solve_5_9(w, cls):
  # Безкоштовна норма залежить від класу
  limit = 20 if cls == "econom" else 30
  # Перевищення ваги, але не менше нуля
  extra = max(0, w - limit)
  # Доплата 15 грн за кожен кілограм перевищення
  return f"{extra * 15:.0f}"

# Тести:
print(solve_5_9(22, "econom"))  # Очікується: 30
print(solve_5_9(40, "business"))  # Очікується: 150
print(solve_5_9(20, "econom"))  # Очікується: 0 (межовий випадок)
print(solve_5_9(30, "business"))  # Очікується: 0 (межовий випадок)