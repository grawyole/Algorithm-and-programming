s = input("Введіть рядок: ")

clean = ""
for ch in s.lower():
    if ch.isalpha():
        clean += ch

palindrome = clean == clean[::-1]

print("так" if palindrome else "ні")