from machine.drink import Drink
from machine.money_machine import MoneyMachine
from colorama import Fore, Style
import time
import sys

class CoffeeMachine:
    def __init__(self, water=300, milk=200, coffee=100, money=100.00):
        self.water = water
        self.milk = milk
        self.coffee = coffee
        self.money = money
        self.money_machine = MoneyMachine()

    def loading_effect(self, message="Processing"):
        print(Fore.MAGENTA + Style.BRIGHT + f"\n{message}", end="")
        for _ in range(3):
            time.sleep(0.5)
            print(Fore.MAGENTA + ".", end="", flush=True)
        print("\n")

    def report(self):
        print(Fore.YELLOW + Style.BRIGHT + "\n📊 MACHINE REPORT")
        print(Fore.YELLOW + "-------------------------")
        print(Fore.BLUE + f"🧊 Water   : {self.water}ml")
        print(Fore.BLUE + f"🥛 Milk    : {self.milk}ml")
        print(Fore.BLUE + f"☕ Coffee  : {self.coffee}g")
        print(Fore.GREEN + f"💰 Money   : ₹{self.money:.2f}")
        print(Fore.YELLOW + "-------------------------")

    def is_resources_sufficient(self, drink_name):
        drink = Drink()
        resources = drink.get_drink_resources(drink_name)

        for resource, amount in resources.items():
            if resource == "Water" and self.water < amount:
                print(Fore.RED + f"❌ Not enough water to prepare {drink_name}.")
                return False
            elif resource == "Milk" and self.milk < amount:
                print(Fore.RED + f"❌ Not enough milk to prepare {drink_name}.")
                return False
            elif resource == "Coffee" and self.coffee < amount:
                print(Fore.RED + f"❌ Not enough coffee to prepare {drink_name}.")
                return False
        return True

    def brew_drink(self, drink_name):
        drink = Drink()
        resources = drink.get_drink_resources(drink_name)
        cost = drink.get_price(drink_name)

        self.loading_effect("💸 Verifying payment")
        if self.money_machine.make_payment(cost):
            self.loading_effect(f"☕ Brewing {drink_name}")
            self.water -= resources.get("Water", 0)
            self.milk -= resources.get("Milk", 0)
            self.coffee -= resources.get("Coffee", 0)
            self.money += cost
            print(Fore.GREEN + Style.BRIGHT + f"✅ {drink_name} is ready. Enjoy your coffee!\n")
            return True
        else:
            print(Fore.RED + "❌ Transaction failed. Please try again.")
            return False

    def exit(self):
        self.loading_effect("Shutting down")
        print(Fore.YELLOW + Style.BRIGHT + "\n👋 Coffee Machine is now off. Have a great day!")
        time.sleep(1)
        sys.exit()
