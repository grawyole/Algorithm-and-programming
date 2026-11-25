import math

a, b = map(int, input().split())

nsd = math.gcd(a, b)
nsk = a * b // nsd

print(f"НСД = {nsd}, НСК = {nsk}")