from machine.ascii_art import art
from machine.menu import Menu
from machine.coffee_machine import CoffeeMachine
from colorama import Fore, Style, init
import time
import os
import sys

init(autoreset=True)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def welcome_banner():
    print(Fore.CYAN + Style.BRIGHT + f"        {art}")

def neon_loader(message="⚙ Processing"):
    dots = ["⠁", "⠂", "⠄", "⠂"]
    print(Fore.MAGENTA + Style.BRIGHT + message, end=" ", flush=True)
    for i in range(8):
        sys.stdout.write(Fore.MAGENTA + dots[i % len(dots)])
        sys.stdout.flush()
        time.sleep(0.2)
        sys.stdout.write("\b")
    print(Fore.MAGENTA + "✔")

def main():
    menu = Menu()
    coffee_machine = CoffeeMachine()

    is_on = True
    while is_on:
        clear_screen()
        welcome_banner()
        menu.get_item()

        user_input = input(Fore.CYAN + Style.BRIGHT + "\nSelect your brew [1-{}]: ".format(len(menu.drink_name))).strip()

        try:
            user_choice = int(user_input)
            if 1 <= user_choice <= len(menu.drink_name):
                selected_item = menu.drink_name[user_choice - 1]

                if selected_item.lower() == "report":
                    coffee_machine.report()
                    input(Fore.WHITE + "\nPress [Enter] to continue...")
                elif selected_item.lower() == "exit":
                    coffee_machine.exit()
                    is_on = False
                else:
                    if coffee_machine.is_resources_sufficient(selected_item):
                        neon_loader(f"Brewing {selected_item}")
                        coffee_machine.brew_drink(selected_item)
                        input(Fore.WHITE + "\nEnjoy ☕ — Press [Enter] to return to menu...")
            else:
                print(Fore.RED + "⚠ Invalid option. Please select from the menu.")
                time.sleep(1.5)
        except ValueError:
            print(Fore.RED + "⚠ Invalid input. Numbers only.")
            time.sleep(1.5)

if __name__ == "__main__":
    main()
