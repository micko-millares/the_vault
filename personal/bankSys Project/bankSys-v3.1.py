# Object-oriented programming; Bank Account, Single User (VERSION 3.1.0)
# Changelog/Planned Changes
# Functions fail-proofed, invalid inputs rejected and function is looped until valid input
# Program is now persistent. Will loop on current running iteration until exited. Values during that session are also cached

import time  # so we can slow it down
import random  # experimenting
from colorama import Fore, Back, Style, init  # coloring purposes

init(autoreset=True)  # so that subsequent outputs reset to neutral state/color
time.sleep(1.0)
print(Fore.GREEN + Style.BRIGHT + "\nTerminal Initializing")
time.sleep(1.0)
print(Fore.GREEN + Style.BRIGHT + "\nTerminal Initialized, Loading Prompt...")


################################################################################################


class bankAccount:
    def __init__(self):
        self.balance = random.randrange(
            500.00, 10000.00, 20
        )  # gotta start somewhere...
        self.wallet = random.randrange(20.00, 10000.00, 10)  # stacks on stacks
        time.sleep(0.5)
        print(Fore.YELLOW + Style.BRIGHT + "\nAccount Created!")
        time.sleep(1)

    def deposit(self):  # risk management boiii
        while True:
            try:
                amt = float(input("\nEnter Deposit Amount: $"))
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
                print(Fore.YELLOW + "\nAvailable Balance: $", self.balance)
                time.sleep(0.5)
                print(Fore.YELLOW + "\nCash on Hand: $", self.wallet)
                break

    def withdraw(self):  # cash money
        while True:
            try:
                amt = float(input("\nEnter Withdrawal Amount: $"))
            except ValueError:
                print(Fore.YELLOW + "\nInvalid Input")
                continue
            if amt > self.balance:
                print(Fore.RED + "\nInsufficient Funds")
            elif amt < 0:
                print(Fore.RED + "\nNegative Inputs not Accepted")
            else:
                self.balance -= amt
                self.wallet += amt
                time.sleep(0.5)
                print(Fore.LIGHTYELLOW_EX + "\nAmount Withdrawn:  $", amt)
                time.sleep(0.5)
                print(Fore.LIGHTGREEN_EX + "\nTransaction Completed!")
                time.sleep(0.5)
                print(Fore.LIGHTGREEN_EX + "\nAvailable Balance:  $", self.balance)
                time.sleep(1)
                print(Fore.LIGHTYELLOW_EX + "\nCash on hand:  $", self.wallet)
                break

    def display(self):  # flex on em
        time.sleep(0.5)
        print(Fore.YELLOW + "\nLoading....")
        time.sleep(1.5)
        print(Fore.YELLOW + "\nAvailable Balance:  $", self.balance)
        time.sleep(1)
        print(Fore.YELLOW + "\nCash on hand:  $", self.wallet)


##########################   FUNCTION DRIVERS BELOW! DO NOT TOUCH    ############################


# Create object for the class above so we can call it in the driver;
acct = bankAccount()

# Function Driver
debounce = True  # a debounce! lets program loop until user somehow breaks program or terminates it
while debounce == True:
    time.sleep(0.8)
    userInput = str(
        input(
            "\nType 'deposit' to deposit funds, 'withdraw' for withdrawals, 'display' to view available funds, 'exit' to exit terminal \n"
        )
    ).lower()  # converts every character in userInput regardless of how user typed out response (i.e DePosIt would become deposit), thx mike
    list = ["deposit", "withdraw", "display", "exit"]
    if userInput not in list:
        time.sleep(0.5)
        print(Fore.YELLOW + "Input not recognized. Try again.")  # asks for valid input
    elif userInput == "deposit":  # does callback to deposit function (line 27)
        acct.deposit()
    elif userInput == "withdraw":  # does callback to withdraw function (line 50)
        acct.withdraw()
    elif userInput == "display":  # does callback to display function (line 74)
        acct.display()
    elif userInput == "exit":  # safely terminates program
        time.sleep(0.5)
        debounce = False  # proper loop termination (in this case)
        print(Fore.RED + Style.BRIGHT + "\nSession Terminated")
    else:  # only if someone/something messed \up
        debounce = False  # stops loop on critical error (a separate case)
        print(Fore.RED + "\n Critical Error")

# end

