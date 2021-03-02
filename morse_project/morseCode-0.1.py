# v 0.1, Keyboard-to-morse
#Imports
from pynput import keyboard
from playsound import playsound
import time

def on_release(key):
     time_elapsed = round(time.time() -t, 3)
     print(key, "was depressed for", time_elapsed, "seconds")
    

def on_press(key):
    return False

with keyboard.Listener(on_press=on_press) as press_listener:
    press_listener.join()

t = time.time()

with keyboard.Listener(on_release = on_release) as release_listener:
    release_listener.join()

