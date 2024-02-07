import sys
input = sys.stdin.readline

word = list(map(str, input().strip()))
ww = list(map(str, input().strip()))
stack = []

for char in word:
    stack.append(char)

    # 스택의 끝 부분이 찾고자 하는 문자열과 일치하는지 확인
    if stack[-len(ww):] == list(ww):
        # 일치하면 스택에서 해당 부분을 제거
        for _ in range(len(ww)):
            stack.pop()

if stack == []:
    print('FRULA')
else:
    print(''.join(stack))