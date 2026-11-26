s = input("Введіть рядок: ")

words = s.split()
longest = ""
for w in words:
    if len(w) > len(longest):
        longest = w

print(f"кількість слів = {len(words)}, найдовше \"{longest}\"")