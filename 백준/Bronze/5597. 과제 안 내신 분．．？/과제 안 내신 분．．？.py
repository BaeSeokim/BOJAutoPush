d = [0 for _ in range(31)]

for j in range(28):
    x = int(input())
    d[x] = 1


for y in range(1,31):
    if d[y] == 0:
        print(y)

