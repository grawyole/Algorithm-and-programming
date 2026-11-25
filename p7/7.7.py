s = "тел. 380-67-123"

result = ""
count = 0
for ch in s:
    if ch in "0123456789":
        result = result + "#"
        count += 1
    else:
        result = result + ch

print(f'"{result}", замін {count}')