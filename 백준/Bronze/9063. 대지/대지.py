n = int(input())
c = []
d = []
if n == 1:
    print(0)
else :
    for i in range(n):
        a, b = list(map(int, input().split()))
        c.append(a)
        d.append(b)
    e = (int(max(c))-int(min(c)))
    f = (int(max(d))-int(min(d)))
    print(e*f)