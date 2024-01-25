A, B, V = map(int, input().split())

DAY = ((V - B - 1) // (A - B)) + 1
print(DAY)