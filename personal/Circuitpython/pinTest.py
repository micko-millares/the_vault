# Morse Code LCD Thingy
# test code, imports for use with Metro M0 Express ONLY
import board
import digitalio
import analogio
import time

D2 = digitalio.DigitalInOut(board.D2)
D2.direction = digitalio.Direction.OUTPUT
D2.value = True
A1 = analogio.AnalogIn(board.A1)

def voltage_in_mV(pin):
    return pin.value * 3.3/65536 * 1000

while True:
    print("v(A1) = {} millivolts".format(voltage_in_mV(A1)))
    time.sleep(0.1)
