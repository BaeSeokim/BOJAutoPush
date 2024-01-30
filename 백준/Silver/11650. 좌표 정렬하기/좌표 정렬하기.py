import sys
input = sys.stdin.readline

a = int(input())
c = []
for i in range(a):
    b = list(map(int, input().split()))
    c.append(b)
c.sort()
for j in range(a):
    print(*c[j])