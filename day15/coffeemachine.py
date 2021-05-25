MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = []

available_resource = resources.copy()

def getIngredients_and_cost(selected_coffee):
    user_coffee_name = selected_coffee
    for coffee,value in MENU.items():
        if coffee == selected_coffee:
            coffee = value
            result = getCoffee(coffee,user_coffee_name)
    return result

def getCoffee(selected_coffee,coffee_name):
    for keys,values in selected_coffee.items():
        if keys == "ingredients":
            ingredients = values
            for k,v in ingredients.items():
                if k == "water":
                    water = v
                if k == "milk":
                    milk = v
                if k == "coffee":
                    coffee = v
        if keys == "cost":
            cost = values
    if coffee_name == "espresso":
        return water,coffee,cost
    else:
        return water,milk,coffee,cost

def getAvailableResources():
    for resource_key, resource_value in available_resource.items():
        if resource_key == "water":
            water = resource_value
        if resource_key == "milk":
            milk = resource_value
        if resource_key == "coffee":
            coffee = resource_value
    return water,milk,coffee



# latte price = 2.50, 200ml water, 24g coffee, 150ml milk
# espresso price = 1.50, 50ml water, 18g coffee
# cappuccino price = 3.00, 250ml water, 24g coffee, 100ml milk
def checkResourceSufficient(coffee_selected):
    water,milk,coffee = getAvailableResources()
    if coffee_selected == "latte":
        if water < 200:
            print("Sorry there is not enough water")
            return False
        elif milk < 150:
            print("Sorry there is not enough milk")
            return False
        elif coffee < 24:
            print("Sorry there is not enough coffee")
            return False
        else:
            return True
    if coffee_selected == "cappuccino":
        if water < 250:
            print("Sorry there is not enough water")
            return False
        elif milk < 100:
            print("Sorry there is not enough milk")
            return False
        elif coffee < 24:
            print("Sorry there is not enough coffee")
            return False
        else:
            return True
    if coffee_selected == "espresso":
        if water < 50:
            print("Sorry there is not enough water")
            return False
        elif coffee < 18:
            print("Sorry there is not enough coffee")
            return False
        else:
            return True

def processCoins(selected_coffee):
    result = checkResourceSufficient(selected_coffee)
    if result:
        print("Please insert coins")
        quarters = int(input("how many quarters?: "))
        dimes = int(input("how many dimes?: "))
        nickles = int(input("how many nickles?: "))
        pennies = int(input("how many pennies?: "))
        totalmoney = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01

        if selected_coffee == "espresso" and totalmoney < 1.50:
            print("Sorry that's not enough money. Money refunded")
        elif selected_coffee == "latte" and totalmoney < 2.50:
            print("Sorry that's not enough money. Money refunded")
        elif selected_coffee == "cappuccino" and totalmoney < 3.00:
            print("Sorry that's not enough money. Money refunded")
        else:

            result = getIngredients_and_cost(selected_coffee)
            available_water, available_milk, available_coffee = getAvailableResources()
            if selected_coffee == "espresso":
                water,coffee,coffee_cost = result
                newAvailableResources = {"water": available_water - water, "milk": available_milk,
                                         "coffee": available_coffee - coffee}
            else:
                water,milk,coffee,coffee_cost = result
                newAvailableResources = {"water": available_water - water, "milk": available_milk - milk,
                                         "coffee": available_coffee - coffee}
            returnchange =  totalmoney - coffee_cost
            money.append(coffee_cost)
            available_resource.update(newAvailableResources)
            if returnchange > 0.00:
                print(f"Here is ${returnchange} in change")
                print(f"Here is your {selected_coffee} Enjoy")
            else:
                print(f"Here is your {selected_coffee} Enjoy")



is_exit = False
while not is_exit:
    user_input = input("What would you like? (espresso/latte/cappuccino): ")
    if user_input == "report":
        water,milk,coffee = getAvailableResources()
        totalmoney = sum(money)
        print(f"Water: {water}ml \nMilk: {milk}ml \nCoffee: {coffee}g \nMoney: ${totalmoney}")
    elif user_input == "off":
        is_exit = True
    else:
        processCoins(user_input)