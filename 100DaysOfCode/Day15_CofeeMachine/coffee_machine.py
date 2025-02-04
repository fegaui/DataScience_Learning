#TODO 1 keep a list record of all the ingredients remaining and all the money in the machine
from menu import ware_house, menu, coins

def check_resources(user_request, menu):
    '''Takes the user input and the values of the ingredients in the menu
       checks for the ingredients
       returns a list with a boolean and the ingredient missing
    '''
    for key in menu[user_request]["ingredients"]:
        check = ware_house[key] >= menu[user_request]["ingredients"][key]
        if not check:
            return [check, key]        
    return [check, ""]

def deduct(resources, user_request):
    """The input is the dict that keeps the amount of resources and the user requested coffee"""
    for key in resources:
        resources[key] -= menu[user_request]["ingredients"][key]
    return resources

def check_input(user_request, menu, cash_regist, ware_house):
    if user_request == "report":
        print(f"Water: {ware_house['water']} ml")
        print(f"Milk: {ware_house['milk']} ml")
        print(f"coffee: {ware_house['coffee']} g")
        print(f"Money: ${cash_regist}")

    elif user_request == "off":
        return 0
    
    else:

        if not check_resources(user_request, menu)[0]:
            print(f"Sorry there is not enough {check_resources(user_request, menu)[1]}.")
            return 0 

        else:
            print("Please insert your coins.")
            income_money = 0
            for key in coins:
                number_of_coins = int(input(f"How many {key}?"))
                income_money += coins[key]*number_of_coins
            
            if income_money >= menu[user_request]["price"]:

                cash_regist += menu[user_request]["price"]
                change = income_money - menu[user_request]["price"]
                print(f"Here is ${round(change)} in change.")

                ware_house = deduct(ware_house, user_request)
                print(f"Here is your {user_request} ☕. Enjoy")

            else:
                print("Sorry that's not enough money. Money refunded.")
    return cash_regist




#TODO 2 prompt the user "What would you like? (espresso/latte/cappuccino): "

user_request = ""
cash_regist = 0

while user_request != 'off':
    user_request = input("What would you like? (espresso/latte/cappuccino):  ").lower().strip()
    cash_regist = check_input(user_request, menu, cash_regist, ware_house)

    









