n = int(input())
count = n
for i in range(n):
    x = input()
    for j in range(0,len(x)-1):
        if x[j] == x[j+1] :
            pass
        else : 
            if x[j] in x[j+1:]:
                count -= 1
                break
print(count)    