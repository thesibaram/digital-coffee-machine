class MoneyMachine:
    CURRENCY = "₹"

    COINS = {
        "10 rupee": 10,
        "5 rupee": 5,
        "2 rupee": 2,
        "1 rupee": 1
    }

    def process_coins(self, cost):
        print(f"Please insert coins. (Cost: {self.CURRENCY}{cost:.2f})")
        total = 0
        for coin, value in self.COINS.items():
            while True:
                try:
                    num = int(input(f"How many {coin} coins?: "))
                    total += num * value
                    break
                except ValueError:
                    print("❌ Invalid input. Please enter a number.")
        return round(total, 2)

    def make_payment(self, cost):
        total_inserted = self.process_coins(cost)
        if total_inserted >= cost:
            change = round(total_inserted - cost, 2)
            if change > 0:
                print(f"💰 Change returned: {self.CURRENCY}{change}")
            return True
        else:
            print(f"❌ Not enough money. You entered {self.CURRENCY}{total_inserted}. Money refunded.")
            return False
