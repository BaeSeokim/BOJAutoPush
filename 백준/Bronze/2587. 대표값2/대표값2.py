lst = []
for _ in range(5):
    n = int(input())
    lst.append(n)
lst.sort()
print(sum(lst)//5)
print(lst[2])