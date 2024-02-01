import sys
input = sys.stdin.readline

n = int(input())
cnt = 0
arr = set()

for i in range(n):
    a = input().rstrip()
    if a == 'ENTER':
        arr = set()
    elif a not in arr:
        cnt += 1
        arr.add(a)
print(cnt)
    