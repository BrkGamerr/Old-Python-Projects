from menu_and_resources import menu
from menu_and_resources import resources

# User data.
user_choice = ""
user_money = 0

# Lets the user choose the coffee type.
def choose_coffee():

    global user_choice

    if resources["water"] >= 250:
        user_choice = input("\nWelcome to the Coffee Machine!\n\nWhat would you like to get?"
                            "\nEspresso | Latte | Cappuccino: ").lower()

    elif resources["water"] >= 200:
        user_choice = input("\nWelcome to the Coffee Machine!\n\nWhat would you like to get?"
                            "\nEspresso | Latte: ").lower()

    elif resources["water"] >= 50:
        user_choice = input("\nWelcome to the Coffee Machine!\n\nWhat would you like to get?"
                            "\nAt the moment, we only have:"
                            "\nEspresso: ").lower()

    else:
        print("\nSorry, we're currently out of resources.")
        print(f"\nMachine currently has:"
              f"\n\nWater: {resources['water']}ml"
              f"\nMilk: {resources['milk']}ml"
              f"\nCoffee: {resources['coffee']}g"
              f"\nMoney: ${resources['money']}")
        exit()


# Asks the user for money.
def insert_coins():

    global user_money

    user_money += 0.25 * int(input("\nHow many quarters: "))
    user_money += 0.10 * int(input("How many dimes: "))
    user_money += 0.05 * int(input("How many nickles: "))
    user_money += 0.01 * int(input("How many pennies: "))


# Machine processes the order.
def process_the_order():

    global user_choice

    if user_choice == "espresso":
        resources["water"] -= menu["espresso"]["ingredients"]["water"]
        resources["coffee"] -= menu["espresso"]["ingredients"]["coffee"]
        resources["money"] += menu["espresso"]["price"]

    elif user_choice == "latte":
        resources["water"] -= menu["latte"]["ingredients"]["water"]
        resources["coffee"] -= menu["latte"]["ingredients"]["coffee"]
        resources["milk"] -= menu["latte"]["ingredients"]["milk"]
        resources["money"] += menu["latte"]["price"]

    elif user_choice == "cappuccino":
        resources["water"] -= menu["cappuccino"]["ingredients"]["water"]
        resources["coffee"] -= menu["cappuccino"]["ingredients"]["coffee"]
        resources["milk"] -= menu["cappuccino"]["ingredients"]["milk"]
        resources["money"] += menu["cappuccino"]["price"]


# Gives the customer his coffee and change.
def give_coffee():

    global user_money

    change = user_money - menu[user_choice]["price"]
    user_money = 0

    print(f"\nHere's your change: ${change:.2f}.")
    print(f"\nEnjoy your {user_choice.capitalize()}! ☕")


# Coffee Machine.
while True:

    choose_coffee()

    if user_choice == "off":
        exit()

    elif user_choice == "report":
        print(f"\nMachine currently has:"
              f"\n\nWater: {resources['water']}ml"
              f"\nMilk: {resources['milk']}ml"
              f"\nCoffee: {resources['coffee']}g"
              f"\nMoney: ${resources['money']}")
        continue

    insert_coins()
    process_the_order()
    give_coffee()
