i = int(input())
cnt = 2
for j in range(i):
    cnt += (2**j)

print(cnt**2)