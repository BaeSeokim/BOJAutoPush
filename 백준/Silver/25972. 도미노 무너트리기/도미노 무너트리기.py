import sys
input = sys.stdin.readline

N = int(input())
# domino = [list(map(int,input().split())) for i in range(N)]
domino = sorted([list(map(int,input().split())) for i in range(N)], key = lambda x:x[0])
count = 0
    
for i in range(N-1):
    if domino[i][0]+domino[i][1] < domino[i+1][0]:
        count += 1
    else:
        continue
    
print(count+1)