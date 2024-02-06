import sys
input = sys.stdin.readline

a, b = map(int, input().split())
c = a-b
if c <= 0:
    c = c * (-1)
print(c)