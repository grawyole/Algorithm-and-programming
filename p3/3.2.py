s = int(input())

h = s // 3600
m = s % 3600 // 60
sec = s % 60

print(f"{h}:{m:02d}:{sec:02d}")