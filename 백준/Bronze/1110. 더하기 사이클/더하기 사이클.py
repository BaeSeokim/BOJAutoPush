import sys
input = sys.stdin.readline
cc = input().strip()
if cc == '0':
    print(1)
elif 1 <= int(cc) <= 9:
    a = 0
    b = int(cc)
    c = a
    d = b
    cnt = 0
    while True:
        tmp = b
        if (a + b) >= 10:
            b = (a + b) % 10
        else:
            b = (a + b)
        a = tmp
        cnt += 1
        if a == c and b == d:
            break
    print(cnt)
else:
    a = int(cc[0])
    b = int(cc[1])

    c = a
    d = b
    cnt = 0
    while True:
        tmp = b
        if (a+b) >= 10:
            b = (a + b) % 10
        else:
            b = (a + b)
        a = tmp
        cnt += 1
        if a == c and b == d:
            break
    print(cnt)