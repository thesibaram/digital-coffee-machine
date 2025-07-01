from tests.test_menu import Menu
from tests.test_machine import CoffeeMachine

def main():
    menu = Menu()
    coffee_machine = CoffeeMachine()

    is_on = True
    while is_on:
        menu.get_item()
        user_input = input("What would you like to order? (Enter number): ").strip()

        try:
            user_choice = int(user_input)
            if 1 <= user_choice <= len(menu.drink_name):
                selected_item = menu.drink_name[user_choice - 1]

                if selected_item == "Report":
                    coffee_machine.report()
                elif selected_item == "Exit":
                    coffee_machine.exit()
                    is_on = False
                else:
                    if coffee_machine.is_resources_sufficient(selected_item):
                        coffee_machine.brew_drink(selected_item)
            else:
                print("Invalid selection. Please choose a number from the menu.")
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
