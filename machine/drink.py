from colorama import Fore, Style

class Drink:
    def __init__(self):
        self.__drink_name_cost = {
            "Espresso": 50,
            "Americano": 70,
            "Cappuccino": 90,
            "Latte": 100
        }

        self.__resources = {
            "Espresso": {
                "Water": 50,
                "Coffee": 18
            },
            "Americano": {
                "Water": 100,
                "Coffee": 24,
                "Milk": 150
            },
            "Cappuccino": {
                "Water": 200,
                "Coffee": 24,
                "Milk": 150
            },
            "Latte": {
                "Water": 250,
                "Coffee": 24,
                "Milk": 150
            }
        }

    def get_price(self, drink_name):
        """Returns the cost of a specific drink."""
        return self.__drink_name_cost.get(drink_name)

    def get_drink_resources(self, drink_name):
        """Returns the resources needed for a specific drink."""
        return self.__resources.get(drink_name)

    def get_all_drinks(self):
        """Returns a list of all drink names."""
        return list(self.__drink_name_cost.keys())

    def print_menu(self):
        """Prints drink names and their prices."""
        print(Fore.YELLOW + Style.BRIGHT + "\n📋 Drink Menu:")
        print(Fore.YELLOW + "--------------------------")
        for idx, (name, cost) in enumerate(self.__drink_name_cost.items(), start=1):
            print(Fore.CYAN + f"{idx}. {name}: ₹{cost}")
