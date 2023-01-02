MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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
    "money": 0,
}


def coffee_machine():

    on = True
    while on:

# TODO 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
        drink = input("What would you like? (espresso/latte/cappuccino): ").lower()

# TODO 2. Turn off the Coffee Machine by entering “off” to the prompt.
        if drink == "off":
            return

# TODO 3. Print report.
        if drink == "report":
            print(f"Water: {resources['water']}ml")
            print(f"Milk: {resources['milk']}ml")
            print(f"Coffee: {resources['coffee']}g")
            print(f"Money: ${resources['money']}")
            continue

# TODO 4. Check resources sufficient?
        if drink not in MENU:
            continue
        if resources["water"] < MENU[drink]["ingredients"]["water"]:
            print("Sorry, there is not enough water.")
            continue
        elif resources["coffee"] < MENU[drink]["ingredients"]["coffee"]:
            print("Sorry, there is not enough coffee.")
            continue
        elif resources["milk"] < MENU[drink]["ingredients"]["milk"]:
            print("Sorry, there is not enough milk.")
            continue
        else:
            print("Please insert coins.")

# TODO 5. Process coins.
        quarters = int(input("How many quarters?: ")) * 0.25
        dimes = int(input("How many dimes?: ")) * 0.10
        nickles = int(input("How many nickles?: ")) * 0.05
        pennies = int(input("How many pennies?: ")) * 0.01
        cash = quarters + dimes + nickles + pennies

# TODO 6. Check transaction successful?
        if cash < MENU[drink]["cost"]:
            print("Sorry, that is not enough money. Money refunded.")
            continue
        elif cash > MENU[drink]["cost"]:
            change = round((cash - MENU[drink]["cost"]), 2)
            print(f"Here is ${change} in change.")

# TODO 7. Make Coffee.
        resources["water"] -= MENU[drink]["ingredients"]["water"]
        resources["coffee"] -= MENU[drink]["ingredients"]["coffee"]
        resources["milk"] -= MENU[drink]["ingredients"]["milk"]
        resources["money"] += MENU[drink]["cost"]
        print(f"Here is your {drink} ☕️. Enjoy!")

coffee_machine()