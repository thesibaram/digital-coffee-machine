from machine.drink import Drink
from colorama import Fore, Style

class Menu:
    def __init__(self):
        self.drink = Drink()
        self.drink_name = [
            "Espresso",
            "Americano",
            "Cappuccino",
            "Latte",
            "Report",
            "Exit"
        ]

    def display_menu_title(self):
        print(Fore.YELLOW + Style.BRIGHT + "\n☕ Available Options ☕")
        print(Fore.YELLOW + "---------------------------")

    def get_item(self):
        self.display_menu_title()
        for index, item in enumerate(self.drink_name, start=1):
            if item not in ["Report", "Exit"]:
                price = self.drink.get_price(item)
                price_tag = f" (₹{price:.2f})"
                print(Fore.CYAN + f"{index}. {item}{price_tag}")
            else:
                print(Fore.CYAN + f"{index}. {item}")


