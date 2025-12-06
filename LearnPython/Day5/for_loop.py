student_scores = [150,142,185,120,171,184,149,24,59,68,199,78,65,89,86]

sum = sum(student_scores)
top_scorer = max(student_scores)

print(sum)
print(top_scorer)

sum1 =0
temp =0
for score in student_scores:
    if score > temp:
        temp = score
    sum1 += score

print(sum1)
print(temp)

#range() in python 
#range(1,10) -> 10 not included
#range(1,10,3) -> range will step with that number -> 1, 4, 7

for number in range(1,11,3):
    print(number)
