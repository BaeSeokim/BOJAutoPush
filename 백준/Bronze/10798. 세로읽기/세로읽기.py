word = []

for i in range(5):
    word.append([])
    wo = input()

    for j in range(len(wo)):
        word[i].append(wo[j])
    for k in range(len(wo),15):
        word[i].append('')
z = ''   
for x in range(15):
    z += word[0][x] + word[1][x] + word[2][x] + word[3][x] + word[4][x]
print(z)