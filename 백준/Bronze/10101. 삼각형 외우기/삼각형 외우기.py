a = int(input())
b = int(input())
c = int(input())
if(a+b+c)==180:
    if a == b == c:
        print('Equilateral')
    elif a == b:
        if a != c:
            print('Isosceles')
    elif a == c:
        if a != b:
            print('Isosceles')
    elif c == b:
        if a != c:
            print('Isosceles')
    else :
        print('Scalene')
    

else:
    print('Error')
    
