import sys
input = sys.stdin.readline

n = int(input())
lst = [0] * 10001
for i in range(n):
    a = int(input().rstrip())
    lst[a] += 1

for i in range(10001):
    for _ in range(lst[i]):
        print(i)