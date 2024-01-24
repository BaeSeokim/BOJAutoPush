n = int(input())

a = 1
b = 0
for i in range(n):
    sum_a = a
    sum_b = b
    
    a = b
    b = sum_a + sum_b
    
print(a, b)