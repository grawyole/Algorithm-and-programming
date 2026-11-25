p, r = map(float, input().split())

result = p * (1 + r / 100) ** 3

print(f"{result:.2f}")