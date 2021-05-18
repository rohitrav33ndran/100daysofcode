# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇


name1 = name1.lower()
name2 = name2.lower()
name = name1+name2
t = name.count("t")
r = name.count("r")
u = name.count("u")
e = name.count("e")
l = name.count("l")
o = name.count("o")
v = name.count("v")
e = name.count("e")

truecount = t + r + u + e
lovecount = l + o + v + e
truelove = str(truecount)+str(lovecount)

if int(truelove) < 10 or int(truelove) > 90:
  print(f"Your score is {truelove}, you go together like coke and mentos.")

elif int(truelove) >= 40 and int(truelove) <= 50:
  print(f"Your score is {truelove}, you are alright together.")

else:
  print(f"Your score is {truelove}.")
