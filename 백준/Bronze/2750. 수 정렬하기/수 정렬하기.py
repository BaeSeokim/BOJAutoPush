n = int(input())
d = []
for i in range(n):
    x = int(input())
    d.append(x)
    
d.sort()

for i in range(n):
    print(d[i])