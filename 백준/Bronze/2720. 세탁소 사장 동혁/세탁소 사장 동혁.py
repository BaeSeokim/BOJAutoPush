t = int(input())

for _ in range(t):
    money = int(input())
    arr = []
    a = money//25
    arr.append(a)
    money = money % 25
    b = money//10
    arr.append(b)
    money = money % 10
    c = money // 5
    arr.append(c)
    money = money % 5
    d = money // 1
    arr.append(d)
    print(*arr)