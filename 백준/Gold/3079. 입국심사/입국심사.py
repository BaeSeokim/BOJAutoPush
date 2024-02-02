import sys 
input = sys.stdin.readline

n, m = map(int, input().split())
lst = [int(input()) for _ in range(n)]

l, r = min(lst), max(lst) * m
ans = r

while l <= r:
    total = 0
    mid = (l + r) // 2

    for i in range(n):
        total += mid // lst[i]

    if total >= m:
        r = mid -1
        ans = min(mid, ans)

    else:
        l = mid + 1

print(ans)