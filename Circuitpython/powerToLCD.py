# Voltage to LCD Display Code
import time
import board
import digitalio
import analogio
import busio
import adafruit_character_lcd.character_lcd as characterlcd

# Modify this if you have a different sized character LCD
lcd_columns = 16
lcd_rows = 2

# Metro M0/M4 Pin Config:
lcd_rs = digitalio.DigitalInOut(board.D7)
lcd_en = digitalio.DigitalInOut(board.D8)
lcd_d7 = digitalio.DigitalInOut(board.D12)
lcd_d6 = digitalio.DigitalInOut(board.D11)
lcd_d5 = digitalio.DigitalInOut(board.D10)
lcd_d4 = digitalio.DigitalInOut(board.D9)
lcd_backlight = digitalio.DigitalInOut(board.D13)

# Initialise the LCD class
lcd = characterlcd.Character_LCD_Mono(
    lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows, lcd_backlight
)

# IMPORTANT STUFF
A1 = analogio.AnalogIn(board.A1)
lcd.backlight = True
resistor_rating = 10000


def voltage_only(pin):  # IN millivolts??
    return pin.value * 3.3 / 65536 * 1000


def voltage_to_watts(pin):  # IN WATTS
    return ((pin.value * 3.3 / 65536) ** 2) / resistor_rating


while True:
    # print("v(A1) = {:6.2f} milliWatts".format(round(voltage_to_watts(A1), 2)))
    time.sleep(1)
    print((voltage_only(A1),))
    lcd.clear()
    lcd.message = str(
        "Output: \n{} mW".format(round(voltage_to_watts(A1), 2))
    )  # Rounded to two decimal places
    time.sleep(0.16)  # 0.1 for testing purposes, 0.2-0.3 for readability

