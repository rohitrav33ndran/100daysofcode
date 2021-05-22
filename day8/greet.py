# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.


# def greet():
#   for i in range(3):
#     print(f"Print {i}")

# greet()

def greet_with_input(name,location):
  print(f"Hi {name}, How do you do?")
  print(f"How is the weather in your city {location}")

greet_with_input("Rohit","Chennai")
greet_with_input(location="Berlin",name="Binsha")
