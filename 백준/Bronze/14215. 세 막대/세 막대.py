a, b, c = map(int, input().split())
f = max(a,b,c)
d = min(a,b,c)
e = a+b+c-f-d
if d + e <= f:
    print(d+e+d+e-1)
else:
    print(d+e+f)
