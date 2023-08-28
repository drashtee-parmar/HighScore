# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

### the higest value for student score
# max_student_score = max(student_scores)
# print(max_student_score)

##### The lowest value for student score
# min_student_score = min(student_scores)
# print(f"The lowest student score is: {min_student_score}.")


# student_scores = [78, 65, 89, 86, 55, 91, 64, 89]
#### Using for loop #####
highest_score = 0

for score in student_scores:
    if score > highest_score:
        highest_score = score
print(f"The highest score in the class is: {highest_score}")





