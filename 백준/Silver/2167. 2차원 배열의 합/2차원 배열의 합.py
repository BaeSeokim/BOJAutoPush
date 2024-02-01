import sys
input = sys.stdin.readline

a, b = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(a)]

# 누적 합 배열을 계산합니다.
prefix_sum = [[0] * (b + 1) for _ in range(a + 1)]
for i in range(1, a + 1):
    for j in range(1, b + 1):
        prefix_sum[i][j] = prefix_sum[i - 1][j] + prefix_sum[i][j - 1] - prefix_sum[i - 1][j - 1] + lst[i - 1][j - 1]

t = int(input())

for _ in range(t):
    c, d, e, f = map(int, input().split())

    # 배열의 합을 계산합니다.
    result = prefix_sum[e][f] - prefix_sum[c - 1][f] - prefix_sum[e][d - 1] + prefix_sum[c - 1][d - 1]
    
    print(result)
