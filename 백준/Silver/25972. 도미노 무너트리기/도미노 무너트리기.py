import sys
input = sys.stdin.readline
n = int(input())
domi = []
for i in range(n):
    x, y = map(int, input().split())
    domi.append((x, y))
domi.sort()
count = 0

for i in range(n-1):
    if domi[i][0]+domi[i][1] < domi[i+1][0]:
        count += 1 

print(count+1)

