import sys

n, m = map(int, sys.stdin.readline().split())
basket = []
    
for i in range(n):
    basket.append(i+1)


for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    basket[x-1],basket[y-1] = basket[y-1],basket[x-1]

for a in basket:
    print(a, end=' ')
