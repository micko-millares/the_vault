# Here goes nothing

from tkinter import Tk, Label, Button

# Important stuff
class firstGUI:
    def __init__(self, master):
        self.master = master
        master.title("First GUI")

        self.label = Label(master, text="Trying it out")
        self.label.pack()

        self.greet_button = Button(master, text="Hello", command=self.Hello)
        self.greet_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

        self.master.geometry("800x600")

    def Hello(self):
        print("WASSUP")


root = Tk()
my_gui = firstGUI(root)
root.mainloop()
