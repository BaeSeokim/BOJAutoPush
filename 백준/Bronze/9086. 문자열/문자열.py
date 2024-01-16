n = int(input())
sen = []
for _ in range(n):
    x = input()   
    sen.append(x)

for i in range(n):
    print(sen[i][:1] + sen[i][::-1][:1])