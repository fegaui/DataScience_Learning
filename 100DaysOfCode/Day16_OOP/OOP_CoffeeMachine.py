from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

off = False
coffe_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu_obj = Menu()

while not off:
    
    user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()
   

    if user_input == "off":
        off = True
    elif user_input == "report":
        coffe_maker.report()
        money_machine.report()
    else:
        drink_order = menu_obj.find_drink(user_input)

        if coffe_maker.is_resource_sufficient(drink_order) and money_machine.make_payment(drink_order.cost): 
                coffe_maker.make_coffee(drink_order)
        else:
            continue

        

