
n ,b = input().split()
n = n[::-1]

nb = 0

for i in range(len(n)):
    if ord(n[i]) < 65:
        nb += int(n[i])*int(b)**i
    else :
        nb += ((ord(n[i]))-55) *int(b)**i
        
print(nb)