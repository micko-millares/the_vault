# v 0.1, Keyboard-to-morse
#Imports
#import keyboard
from pynput.keyboard import Key, Listener
from playsound import playsound
import time

def on_press(key):
    if key == Key.left:
        playsound("click.mp3")
        print('.')
    elif key == Key.right:
        playsound("click.mp3")
        print('-')
        #playsound("morse_dash.mp3")

def on_release(key):
    if key == Key.esc:
        print('Terminating...')
        time.sleep(0.5)
        return False

with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

""" from pynput.keyboard import Key, Listener

def on_press(key):
    print('{0} pressed'.format(
        key))

def on_release(key):
    print('{0} release'.format(
        key))
    if key == Key.esc:
        # Stop listener
        return False

# Collect events until released
with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join() """