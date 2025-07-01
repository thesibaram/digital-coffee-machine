from tests.test_drink import Drink

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

    def get_item(self):
        print("\nAvailable Options:")
        for i, item in enumerate(self.drink_name, start=1):
            price = self.drink.get_price(item) if item not in ["Report", "Exit"] else ""
            print(f"{i}. {item}{f' (₹{price:.2f})' if price else ''}")

