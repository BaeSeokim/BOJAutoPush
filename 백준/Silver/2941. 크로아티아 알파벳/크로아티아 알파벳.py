n = input()
n += 'aaa'
co = 0
for i in range(len(n)-3):
    if n[i] == 'c':
        if n[i+1] == '=':
            co += 1
        if n[i+1] == '-':
            co += 1   
    elif n[i] == 'd':
        if n[i+1] == '-':
            co += 1
        if n[i+1] == 'z':
            if n[i+2] == '=':
                co += 1
    elif n[i] == 'l':
        if n[i+1] == 'j':
            co += 1
    elif n[i] == 'n':
        if n[i+1] == 'j':
            co += 1
    elif n[i] == 's':
        if n[i+1] == '=':
            co += 1
    elif n[i] == 'z':
        if n[i+1] == '=':
            co += 1
    else :
        pass

print(len(n)-co-3)
    