from tests.test_drink import Drink
from tests.test_money import MoneyMachine

class CoffeeMachine:
    def __init__(self, water=300, milk=200, coffee=100, money=100.00):
        self.water = water
        self.milk = milk
        self.coffee = coffee
        self.money = money
        self.money_machine = MoneyMachine()

    def report(self):
        print("\n📊 Machine Report:")
        print(f"Water  : {self.water}ml")
        print(f"Milk   : {self.milk}ml")
        print(f"Coffee : {self.coffee}g")
        print(f"Money  : ₹{self.money:.2f}")

    def is_resources_sufficient(self, drink_name):
        drink = Drink()
        resources = drink.get_drink_resources(drink_name)

        for resource, amount in resources.items():
            if resource == "Water" and self.water < amount:
                print(f"❌ Not enough water for {drink_name}.")
                return False
            elif resource == "Milk" and self.milk < amount:
                print(f"❌ Not enough milk for {drink_name}.")
                return False
            elif resource == "Coffee" and self.coffee < amount:
                print(f"❌ Not enough coffee for {drink_name}.")
                return False
        return True

    def brew_drink(self, drink_name):
        drink = Drink()
        resources = drink.get_drink_resources(drink_name)
        cost = drink.get_price(drink_name)

        if self.money_machine.make_payment(cost):
            print(f"\n☕ Brewing your {drink_name}...")
            self.water -= resources.get("Water", 0)
            self.milk -= resources.get("Milk", 0)
            self.coffee -= resources.get("Coffee", 0)
            self.money += cost
            print(f"✅ {drink_name} is ready. Enjoy!\n")
            return True
        return False

    def exit(self):
        print("👋 Turning off the coffee machine. Goodbye!")
