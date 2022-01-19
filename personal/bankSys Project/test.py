# Object-oriented programming; Bank Account, Single User (VERSION 2.1)
# Changelog/Planned Changes
# Fail protection for class functions: check for valid 'amt' inputs.

import time  # so we can slow it down
import random  # experimenting
from colorama import Fore, Back, Style, init  # coloring purposes

init(autoreset=True)  # so that subsequent outputs reset to neutral state/color
time.sleep(1.5)
print(Fore.GREEN + Style.BRIGHT + "\nTerminal Initializing")
time.sleep(1.5)
print(Fore.GREEN + Style.BRIGHT + "\nTerminal Initialized, Loading Prompt...")


class bankAccount:
    def __init__(self):
        self.balance = random.randrange(500, 10000, 20)  # gotta start somewhere...
        self.wallet = 3000  # stacks on stacks
        time.sleep(0.5)
        print(Fore.YELLOW + Style.BRIGHT + "\nAccount Created!")

    def deposit(self):  # risk management boiii
        while True:
            try:
                amt = float(input("\nEnter Deposit Amount: "))
            except ValueError:
                print(Fore.YELLOW + "\nInvalid Input")
                continue
            if amt > self.wallet:
                print(Fore.RED + "\nNo Cash on Hand!")
                continue
            else:
                self.wallet -= amt
                self.balance += amt
                time.sleep(1.5)
                print(Fore.YELLOW + "\nAmount Deposited: $", amt)
                time.sleep(0.5)
                print(Fore.GREEN + "\nTransaction Completed!")
                time.sleep(0.5)
                print(
                    Fore.YELLOW + "\nAvailable Balance: $",
                    Fore.GREEN + str(self.balance),
                )
                break

    def withdraw(self):  # cash money
        while True:
            try:
                amt = float(input("\nEnter Withdrawal Amount: "))
            except ValueError:
                print(Fore.YELLOW + "\nInvalid Input")
                continue
            if amt > self.balance:
                print(Fore.RED + "\nInsufficient Funds")
            else:
                self.balance -= amt
                self.wallet += amt
                time.sleep(0.5)
                print("\nAmount Withdrawn:  $", amt)
                time.sleep(0.5)
                print("\nTransaction Completed!")
                time.sleep(0.5)
                print("\nAvailable Balance:  $", self.balance)
                time.sleep(1)
                print("\nCash on hand:  $", self.wallet)
                break

    def display(self):  # flex on em
        time.sleep(1.5)
        print("Loading....")
        time.sleep(3)
        print("\nAvailable Balance:  $", self.balance)
        time.sleep(1)
        print("\nCash on hand:  $", self.wallet)


# Object; Class
acct = bankAccount()

# Function Driver
while True:
    userInput = str(
        input(
            "\nType 'deposit' to deposit funds, 'withdraw' for withdrawals, 'display' to view available funds, 'exit' to exit terminal \n"
        )
    )
    list = ["deposit", "withdraw", "display", "exit"]
    if userInput not in list:
        time.sleep(0.5)
        print(Fore.YELLOW + Style.BRIGHT + "Input not recognized. Try again.")
        continue
    else:
        break
if userInput == "deposit":
    acct.deposit()
elif userInput == "withdraw":
    acct.withdraw()
elif userInput == "display":
    acct.display()
elif userInput == "exit":
    time.sleep(0.5)
    print(Fore.RED + Style.BRIGHT + "\nTransaction Terminated")
