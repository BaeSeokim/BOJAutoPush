import sys
input = sys.stdin.readline

a = int(input())
lst = list(map(int, input().split()))
lst.sort()
b = int(input())
lst_ch = list(map(int, input().split()))

for m in lst_ch:
    left = 0
    right = a - 1

    while left <= right:
        mid = (left + right) // 2
        if m > lst[mid]:
            left = mid + 1
        elif m < lst[mid]:
            right = mid -1
        else:
            left = mid
            right = mid
            break
    if left == mid and right == mid:
        print(1)
    else:
        print(0)

