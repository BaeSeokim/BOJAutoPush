n = int(input())

score = list(map(int,input().split()))

max_score = max(score)

lie_score = []
for i in range(n):
       lie_score.append((score[i]/max_score)*100)

print(sum(lie_score)/n)