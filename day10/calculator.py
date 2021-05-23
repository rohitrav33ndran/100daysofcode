import art

print(art.logo)

def add(number1, number2):
    """Adds number1 with number 2"""
    return number1 + number2

def subtract(number1, number2):
    """subtracts number1 with number 2"""
    return number1 - number2

def multiply(number1, number2):
    """multiplies number1 with number 2"""
    return number1 * number2

def divide(number1, number2):
    """divides number1 with number 2"""
    return number1 / number2


def calculator(number1, number2, operation):
    if operation == "+":
        return add(number1, number2)
    elif operation == "-":
        return subtract(number1, number2)
    elif operation == "*":
        return multiply(number1, number2)
    elif operation == "/":
        return divide(number1, number2)
    else:
        return "Invalid operation"

is_new_calc = True
while is_new_calc:
    number1 = float(input("Enter the first number : "))
    print(art.operation_logo)
    operation = input("Pick an operation : ")
    number2 = float(input("Enter the second number : "))
    #invole calc and while loop until no new operation
    finalnumber = calculator(number1, number2, operation)
    print(f"{number1} {operation} {number2} = {finalnumber}")
    is_continue_calc = True
    while is_continue_calc:
        continue_calc = input(f"Type y to continue calculating with {finalnumber}, or type n to start new calculation : ").lower()
        if continue_calc == 'n':
            is_continue_calc = False
            is_new_calc = True
        else:
            nextnum = float(input("Enter the next number : "))
            nextoperation = input("Pick an operation : ")
            nextfinalnumber = calculator(finalnumber, nextnum, nextoperation)
            print(f"{finalnumber} {nextoperation} {nextnum} = {nextfinalnumber}")

