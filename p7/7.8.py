s = input("Введіть рядок: ")

words = s.split()
result = ""
abbr = ""
for w in words:
    result = result + w.capitalize() + " "
    abbr = abbr + w[0].upper()

print(result.strip(), abbr)