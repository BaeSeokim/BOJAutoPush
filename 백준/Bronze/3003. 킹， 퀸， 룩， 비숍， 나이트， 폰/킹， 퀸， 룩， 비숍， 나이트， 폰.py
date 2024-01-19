arr = list(map(int,input().split()))
real_arr = [1, 1, 2, 2, 2, 8]
result = []

for i in range(6):
    result.append(real_arr[i]-arr[i])

print(*result)