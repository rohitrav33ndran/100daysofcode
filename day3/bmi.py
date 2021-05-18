
# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bmi = round((weight / height ** 2),1)


if bmi < 18.5:
  print("You are underweight")
elif bmi < 25:
  print("Normal Weight")
elif bmi < 30:
  print("slightly overweight")
elif bmi < 35:
  print("Obese")
else:
  print("Clinically Obese")

