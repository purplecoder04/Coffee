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
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
are_you_done = True
#TODO: print report
#todo: check resource sufficient
#todo: Procress coins
#todo: check transaction successful
#todo: make coffee

def do_we_enough(recipe):
    for item in recipe:
        if recipe[item] > resources[item]:
            print(f"Sorry there is not enough{item}.")
            return False
    return True

def show_me_the_money():
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def do_you_have_enough_money(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_drink(drink_name, order_recipe_items):
    for item in order_recipe_items:
        resources[item] -= order_recipe_items[item]
    print(f"Here is your {drink_name} ☕. Enjoy!")


while are_you_done:
    customer_input = input("What would you like? (espresso/latte/cappuccino):").lower()
    if customer_input == "off":
        are_you_done = False
    elif customer_input == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[customer_input]
        if do_we_enough(drink["ingredients"]):
            payment = show_me_the_money()
            if do_you_have_enough_money(payment, drink["cost"]):
                make_drink(customer_input, drink["ingredients"])