s = input("Введіть рядок: ")

filtered = [c for c in s if c != " "]
m_c = max(set(filtered), key=filtered.count) if filtered else ""
count = filtered.count(m_c)

print(f"'{m_c}', {count} разів")