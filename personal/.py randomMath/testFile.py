# Object-oriented programming; Bank Account, Single User (TEST VERSION)

import time  # so we can slow it down
import random  # experimenting
from colorama import Fore, Back, Style, init  # coloring purposes

init(autoreset=True)  # so that subsequent outputs reset to neutral state/color
time.sleep(1.5)
print(Fore.GREEN + Style.BRIGHT + "Terminal Initializing")
time.sleep(1.5)
print(Fore.GREEN + Style.BRIGHT + "Terminal Initialized, Loading Prompt...")


class bankAccount:
    def __init__(self):
        self.balance = random.randrange(500, 10000, 20)  # gotta start somewhere...
        self.wallet = 3000  # stacks on stacks
        print("\nAccount Created!")

    def deposit(self):  # risk management boiii
        amt = float(input("\nEnter Deposit Amount: "))
        if amt > self.wallet:
            print("\nNo cash!")  # broke ass
        else:
            self.wallet -= amt
            self.balance += amt
            time.sleep(1.5)
            print("\nAmount Deposited: ", amt)
            time.sleep(0.5)
            print("\nTransaction Completed!")
            time.sleep(0.5)
            print("\nAvailable Balance: ", self.balance)

    def withdraw(self):  # cash money
        amt = float(input("\nEnter Withdrawal Amount: "))
        if amt > self.balance:
            time.sleep(1.5)
            print("\nFunds Unavailable!")  # broke ass again
        else:
            self.balance -= amt
            self.wallet += amt
            time.sleep(0.5)
            print("\nAmount Withdrawn: ", amt)
            time.sleep(0.5)
            print("\nTransaction Completed!")
            time.sleep(0.5)
            print("\nAvailable Balance: ", self.balance)
            time.sleep(1)
            print("\n Cash on hand: ", self.wallet)

    def display(self):  # flex on em
        time.sleep(1.5)
        print("Loading....")
        time.sleep(3)
        print("\nAvailable Balance: ", self.balance)
        time.sleep(1)
        print("\nCash on hand: ", self.wallet)


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
    if (userInput not in list):
        print("Input not recognized. Try again.")
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
    print(Fore.RED + Style.BRIGHT + "\nTransaction Terminated")
