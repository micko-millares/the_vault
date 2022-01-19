# Morse Code LCD Thingy
# test code, imports for use with Metro M0 Express ONLY
import board
import digitalio
import analogio
import time

D13 = digitalio.DigitalInOut(board.D13)
D13.direction = digitalio.Direction.OUTPUT
D13.value = False
debounce = False

while debounce == False:
    input("Press ENTER to Toggle LED")
    D13.value = True
    time.sleep(0.1)
    D13.value = False
