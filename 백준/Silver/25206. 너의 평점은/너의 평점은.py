score_sum = []
grade_sum = []
for i in range(20):
    title, score, grade = input().split()
    score_sum.append(float(score))
    grade_sum.append(grade)

sg_sum = []
scs = []
for i in range(20):
    if grade_sum[i] == 'A+':
        sg_sum.append(float(score_sum[i])*(4.5))
        scs.append(score_sum[i])
    elif grade_sum[i] == 'A0':
        sg_sum.append(float(score_sum[i])*(4.0))
        scs.append(score_sum[i]) 
    elif grade_sum[i] == 'B+':
        sg_sum.append(float(score_sum[i])*(3.5))
        scs.append(score_sum[i])
    elif grade_sum[i] == 'B0':
        sg_sum.append(float(score_sum[i])*(3.0))
        scs.append(score_sum[i])
    elif grade_sum[i] == 'C+':
        sg_sum.append(float(score_sum[i])*(2.5))
        scs.append(score_sum[i])
    elif grade_sum[i] == 'C0':
        sg_sum.append(float(score_sum[i])*(2.0))
        scs.append(score_sum[i])   
    elif grade_sum[i] == 'D+':
        sg_sum.append(float(score_sum[i])*(1.5))
        scs.append(score_sum[i])
    elif grade_sum[i] == 'D0':
        sg_sum.append(float(score_sum[i])*(1.0))
        scs.append(score_sum[i])
    elif grade_sum[i] == 'F':
        sg_sum.append(float(score_sum[i])*(0))
        scs.append(score_sum[i])      
    else :  
        pass
count1 = 0 
count2 = 0
for x in range(len(scs)):
    count1 += scs[x]
for y in range(len(sg_sum)):
    count2 += sg_sum[y]
count3 = round((count2 / count1), 7)
print(count3)