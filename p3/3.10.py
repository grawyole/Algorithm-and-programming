t, price, vat = map(float, input().split())

base = t * price
tax = base * (vat / 100)
total = base + tax

print(f"без ПДВ: {base:.2f}")
print(f"ПДВ:     {tax:.2f}")
print(f"разом:   {total:.2f}")