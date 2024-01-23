
word = input()

# 대소문자를 구분하지 않기 위해 모든 문자를 소문자로 변환
word = word.lower()

# 알파벳 빈도수를 저장할 딕셔너리 초기화
letter_count = {}

# 각 알파벳의 빈도수 계산
for char in word:
    if char.isalpha():  # 알파벳인 경우에만 처리
        if char in letter_count:
            letter_count[char] += 1
        else:
            letter_count[char] = 1

# 빈도수가 가장 높은 알파벳 찾기
max_count = max(letter_count.values())
max_letters = [char for char, count in letter_count.items() if count == max_count]

# 결과 출력
if len(max_letters) == 1:
    print(max_letters[0].upper())
else:
    print('?')