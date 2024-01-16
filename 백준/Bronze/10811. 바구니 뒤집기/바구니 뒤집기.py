n, m = map(int,input().split())
arr = []
for i in range(n):
    arr.append(i+1)

for i in range(m):
    x, y = map(int,input().split())
    arr[x-1:y] = arr[x-1:y][::-1]

print(*arr)