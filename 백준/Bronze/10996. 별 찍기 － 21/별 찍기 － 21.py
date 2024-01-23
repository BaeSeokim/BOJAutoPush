n = int(input())
for _ in range(n):
    if n % 2 == 0 :
        print('*'+' *'*((n//2)-1))
        print(' *'+' *'*((n//2)-1))
    elif n % 2 ==1 :
        print('*'+' *'*((n//2)))
        print(' *'*((n//2)))