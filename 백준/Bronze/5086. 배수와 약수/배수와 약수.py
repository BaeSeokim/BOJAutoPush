while True:
    a, b = map(int, input().split())

    if a == b == 0:
        break
    elif a > b:
        if float(a/b) == int(a/b):
            print('multiple')
        else:
            print('neither')
    else:
        if float(b/a) == int(b/a):
            print('factor')
        else:
            print('neither')