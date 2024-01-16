x = list(input().split())

y = list(x[0])
z = list(x[1])
y = (y[::-1])
z = (z[::-1])
a = int(int(y[0])*100+int(y[1])*10+int(y[2]))
b = int(int(z[0])*100+int(z[1])*10+int(z[2]))
if a > b:
    print(a)
else :
    print(b)