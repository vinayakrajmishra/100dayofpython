score = input("Please enter score of all students seareated by comma: \n")
score = score.split(sep=",")
highest_score = score[0]
lowest_score = score[0]

for i in range(0, len(score)):
    if highest_score < score[i]:
        highest_score = score[i]
    if lowest_score > score[i]:
        lowest_score = score[i]

print(f"Highest score is : {highest_score}")
print(f"Lowest score is : {lowest_score}")
