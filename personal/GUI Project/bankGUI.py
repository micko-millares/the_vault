# GUI Version of bankSys3.1

import random
import time
from tkinter import Tk, Label, Button, Entry, IntVar, END, W, E, Widget
from colorama import Fore, Back, Style, init

init(autoreset=True)


class acctMain:
    def __init__(self):
        self.balance = random.randrange(100.00, 10000.00, 1)

    def deposit(self):
        while True:
            try:
                amt = float(input("\nEnter Deposit Amount: $"))
            except ValueError:
                print(Fore.YELLOW + "\nInvalid Input")
                continue
            else:
                self.balance += amt
                time.sleep(1.5)
                print(Fore.YELLOW + "\nAmount Deposited: $", amt)
                time.sleep(0.5)
                print(Fore.GREEN + "\nTransaction Completed!")
                time.sleep(0.5)
                print(Fore.YELLOW + "\nAvailable Balance: $", self.balance)
                break

    def withdraw(self):
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
                time.sleep(0.5)
                print(Fore.LIGHTGREEN_EX + "\nAmount Withdrawn: $", amt)
                time.sleep(0.5)
                print(Fore.LIGHTGREEN_EX + "\nTransaction Completed!")
                time.sleep(1)
                print(Fore.LIGHTGREEN_EX + "\nAvailable Balance: $", self.balance)
                break

    def display(self):
        time.sleep(0.5)
        print(Fore.YELLOW + "\nLoading...")
        time.sleep(1.5)
        print(Fore.YELLOW + "\nAvailable Balance: $", self.balance)


# Pack class above into object 'acct'
acct = acctMain()

# Function Driver Integrated into GUI code below
class mainGUI:
    def __init__(self, master):
        self.master = master
        master.title("Bank System v3.1")
        self.master.geometry("800x600")  # window size on start
        self.master.config(bg="#131517")
        self.master.resizable(0, 0)  # window unresizeable

        # balance button
        self.balance_button = Button(master, text="Balance", command=acct.display)
        self.balance_button.grid()

        # deposit button
        self.deposit_button = Button(master, text="Deposit", command=acct.deposit)
        self.deposit_button.grid()

        # withdraw button
        self.withdraw_button = Button(master, text="Withdraw", command=acct.withdraw)
        self.withdraw_button.grid()


# PRIMARY GUI & UPDATE DRIVER DONT TOUCH!
root = Tk()
my_gui = mainGUI(root)
root.mainloop()
