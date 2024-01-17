T = int(input())

for _ in range(T):
    cot, word = input().split()
    for i in word:
        print(i*int(cot), end='')
    print()