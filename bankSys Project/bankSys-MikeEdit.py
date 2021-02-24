# Object-oriented programming; Bank Account, Single User (VERSION 3.0)
# Changelog/Planned Changes
# Functions fail-proofed, invalid inputs rejected and function is looped until valid input

import time  # so we can slow it down
import random  # experimenting
import os

# time.sleep(1.5)
print("\nTerminal Initializing")
# time.sleep(1.5)
print("\nTerminal Initialized, Loading Prompt...")


class bankAccount:
    def __init__(self):
        self.balance = random.randrange(500, 10000, 20)  # gotta start somewhere...
        self.wallet = 3000  # stacks on stacks
        # time.sleep(0.5)
        print("\nAccount Created!")

    def deposit(self):  # risk management boiii
        while True:
            try:
                amt = float(input("\nEnter Deposit Amount: "))
            except ValueError:
                print("\nInvalid Input")
                continue
            if amt > self.wallet:
                print("\nNo Cash on Hand!")
                continue
            else:
                self.wallet -= amt
                self.balance += amt
                # time.sleep(1.5)
                print("\nAmount Deposited: $%.2f" % amt)
                # time.sleep(0.5)
                print("\nTransaction Completed!")
                # time.sleep(0.5)
                print("\nAvailable Balance: $%.2f" % self.balance)
                break

    def withdraw(self):  # cash money
        while True:
            try:
                amt = float(input("\nEnter Withdrawal Amount: "))
            except ValueError:
                print("\nInvalid Input")
                continue
            if amt > self.balance:
                print("\nInsufficient Funds")
            elif amt < 0:
                print("\nAmmount is negative")
            else:
                self.balance -= amt
                self.wallet += amt
                # time.sleep(0.5)
                print("\nAmount Withdrawn:  $%.2f" % amt)
                # time.sleep(0.5)
                print("\nTransaction Completed!")
                # time.sleep(0.5)
                print("\nAvailable Balance:  $%.2f" % self.balance)
                # time.sleep(1)
                print("\nCash on hand:  $%.2f" % self.wallet)
                break

    def display(self):  # flex on em
        # time.sleep(1.5)
        print("\nLoading....")
        # time.sleep(1.5)
        print("\nAvailable Balance:  $%.2f" % self.balance)
        # time.sleep(1)
        print("\nCash on hand:  $%.2f" % self.wallet)


# Create object for the class above so we can call it in the driver;
acct = bankAccount()

# Function Driver
flex = True  # Used for running code
while flex == True:
    userInput = str(
        input(
            "\nType 'deposit' to deposit funds, 'withdraw' for withdrawals, 'display' to view available funds, 'exit' to exit terminal \n"
        )
    ).lower()
    list = ["deposit", "withdraw", "display", "exit", "rob bank"]
    if userInput not in list:  # Tests if userInput is in list
        # time.sleep(0.5)
        print("Input not recognized. Try again.")  # asks for valid input
    elif userInput == "deposit":
        acct.deposit()
    elif userInput == "withdraw":
        acct.withdraw()
    elif userInput == "display":
        acct.display()
    elif userInput == "rob bank":
        print(
            '\nYou walk up to the counter and say: "GIVE ME ALL YOU MONEY!!!!"The clerk then pushes the panic button.\
        \nA cop then rushes through the door shooting you in the head killing you instantly.\
        \n*NOW LOADING DARK SOULS DEATH SCREEN*'
        )
        os.startfile(
            "C:\\Users\\Micko\\Desktop\\maxresdefault.jpg"
        )  # CHANGE THIS TO YOUR OWN DIRC
        flex = False
    elif userInput == "exit":
        # time.sleep(0.5)
        flex = False
        print("\nTransaction Terminated")
    else:
        flex = False  # stops loop
        print("Your shit broke fam")
