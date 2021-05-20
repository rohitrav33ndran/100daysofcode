# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
count = 0
sum_of_studentheight = 0
for studentheight in student_heights:
  count += 1
  sum_of_studentheight += studentheight

average_student_height = round(sum_of_studentheight / count)
print(average_student_height)
