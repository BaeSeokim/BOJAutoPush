size = 101
arr = [ [0] * size for _ in range(size) ]
    
n = int(input())

for i in range(n):
    a,b = map(int,input().split())
    
    for j in range(a,a+10):
        for k in range(b, b+10):
            arr[j][k] = 1

result = 0
for i in arr:
    result += i.count(1)
print(result)