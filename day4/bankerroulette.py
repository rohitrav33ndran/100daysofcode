import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
length_of_list = len(names)
luckyperson = names[random.randint(0,length_of_list-1)]

#luckyperson = random.choice(names)
print(f"{luckyperson} going to buy the meal today")
