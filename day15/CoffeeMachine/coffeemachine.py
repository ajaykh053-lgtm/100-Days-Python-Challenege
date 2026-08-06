MENU = {
    "espresso": {"ingredients": {"water": 50, "coffee": 18}, "cost": 1.5},
    "latte": {"ingredients": {"water": 200, "milk": 150, "coffee": 24}, "cost": 2.5},
    "cappuccino": {
        "ingredients": {"water": 250, "milk": 100, "coffee": 24},
        "cost": 3.0,
    },
}
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
profit = 0
is_on = True


def is_rescource_sufficient(order_ingredient):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in order_ingredient:
        if order_ingredient[item] >= resources[item]:
            print(f"Sorry Ther is not enough {item}")
            return False
        return True


def process_coins():
    """Returns the totalcalculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("How many quarters?:")) * 0.25
    total += int(input("How many dimes?:")) * 0.1
    total += int(input("How many nickel?:")) * 0.05
    total += int(input("How many pennies ?:")) * 0.01
    return total


def is_transaction_successful(money_recived, drink_cost):
    if money_recived >= drink_cost:
        change = round(money_recived - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink["cost"]
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct the ingredients from the resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here's your drink {drink_name} ☕. Enjoy!")


while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino):")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_rescource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
