matrix = []

for i in range(1, 10):
    matrix.append(list(map(int, input().split())))
a = 0
max_row, max_col = 0, 0
for i in range(1,10):
    for j in range(1,10):
        if a <= matrix[i-1][j-1]:
            a = matrix[i-1][j-1]
            max_row = i
            max_col = j
print(a)
print(max_row, max_col)
