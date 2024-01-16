d = []

for i in range(10):
    x = int(input())
    d.append(x%42)

dd = set(d)

print(len(dd))