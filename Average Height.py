# Input a python list of students height
student_heights = input("Please enter all the students heights in CM separated by comma \n").split(sep=",")
try:
    for n in range(0, len(student_heights)):
        student_heights[n] = int(student_heights[n])
except ValueError:
    print(f"You might have entered wrong values.{exit()}")

# Calculating sum of all heights
sum_of_heights = 0
for n in range(0, len(student_heights)):
    sum_of_heights = sum_of_heights + student_heights[n]

# Calculating average height
average_height = sum_of_heights/len(student_heights)

print(f"As per your data the average height is: {average_height}")
