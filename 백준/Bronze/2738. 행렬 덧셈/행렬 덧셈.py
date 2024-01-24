a = []
b = []
x, y = map(int,input().split())

for i in range(x):
    a.append(list(map(int, input().split())))
for i in range(x):
    b.append(list(map(int, input().split())))

for i in range(x):
    s = ''
    for j in range(y):
        s += str(a[i][j] + b[i][j]) + ' '
    print(s)
    