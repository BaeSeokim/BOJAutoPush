S = input()
alpa = [-1] * 26
leng = len(S)

for i in range(leng):
    if alpa[ord(S[i])-97] == -1:
        alpa[ord(S[i])-97] = i

print(*alpa)
