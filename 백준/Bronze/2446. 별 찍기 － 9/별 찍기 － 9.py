n = int(input())
for j in range(n,0,-1):
    print(" "*(n-j) + "*"*((2*j)-1))
for i in range(1,n):
    print(" "*(n-i-1) + "*"*((2*i)+1))