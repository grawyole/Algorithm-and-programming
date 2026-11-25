s = "Hello, World!"
k = 3

result = ""
for ch in s:
    if "a" <= ch <= "z":
        result = result + chr((ord(ch) - ord("a") + k) % 26 + ord("a"))
    elif "A" <= ch <= "Z":
        result = result + chr((ord(ch) - ord("A") + k) % 26 + ord("A"))
    else:
        result = result + ch

print(result)