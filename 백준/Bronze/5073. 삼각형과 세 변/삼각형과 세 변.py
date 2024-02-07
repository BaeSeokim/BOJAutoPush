while True:
    a, b, c = map(int, input().split())
    d = max(a,b,c)
    e = min(a,b,c)
    f = a+b+c-d-e
    if a == 0 and b == 0 and c == 0:
        break
    elif a == b == c:
        print('Equilateral')
    elif d >= e + f:
        print('Invalid')
    elif a == b:
        if a != c:
            print('Isosceles')
    elif a == c:
        if a != b:
            print('Isosceles')
    elif b == c:
        if a != c:
            print('Isosceles')
    else:
        print('Scalene')
