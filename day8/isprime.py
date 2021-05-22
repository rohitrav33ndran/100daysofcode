#Write your code below this line 👇

factorial=[]
def prime_checker(number):
  for i in range(1,number+1):
    if number % i == 0:
      factorial.append(i)
  
  if len(factorial) == 2:
    print(f"{number} is prime")
  else:
    print(f"{number} is not prime")

#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)


# Alternative solution
# def prime_checker(number):
#   is_prime = True
#   for i in range(2,number):
#     if number % i == 0:
#       is_prime = False
#   if is_prime == True:
#     print("It's a prime number")
#   else:
#     print(f"{number} is not prime")

