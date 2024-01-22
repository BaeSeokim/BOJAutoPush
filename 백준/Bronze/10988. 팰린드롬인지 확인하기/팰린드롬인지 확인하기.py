n = input()
empty = []

for i in range(len(n)):
    if n[i] == n[len(n)-i-1]:
        continue
    else :
        empty.append(0)
        
if not empty :
    print(1)
else : 
    print(0)