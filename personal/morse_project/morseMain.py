#### Update Log ####
# 2/27/20: v0.1, Basic sound onKeypress
# 3/3/20: v1.0, Added dot/dash soundfiles
# 3/6/2020: v1.5, Replaced soundfiles w/ internally generated sine wave

#import keyboard
from pynput.keyboard import Key, Listener
from playsound import playsound
from pysinewave import SineWave
import time

sinewave = SineWave(pitch = 15)


def on_press(key):
    if key == Key.left:
        sinewave.play() 
        time.sleep(0.1)
        sinewave.stop()
        #playsound("dot_600.wav"),v1.0
        #print('.')
    elif key == Key.right:
        sinewave.play()
        time.sleep(0.2)
        sinewave.stop()
        #playsound("dash_600.wav"), v1.0
        #print('-')
        #playsound("morse_dash.mp3"), OLD

def on_release(key):
    if key == Key.esc:
        print('Terminating...')
        time.sleep(0.5)
        return False

with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
