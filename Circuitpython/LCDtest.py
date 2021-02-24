"""Simple test for monochromatic character LCD"""
import time
import board
import digitalio
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

# debounce for toggling LCD
debounce = True
lcd.backlight = False

while (
    debounce == True
):  # debounce statement lets LCD turn itself off without additional call to lcd.backlight state
    userInput = input("Press Enter to Toggle LCD")
    print("KeyboardInterrupt, Toggling LCD")
    debounce = False
    time.sleep(1.5)
    lcd.backlight = True
    time.sleep(3.5)
    lcd.message = "Testing."
    time.sleep(0.75)
    lcd.clear()
    lcd.message = "Testing.."
    time.sleep(0.75)
    lcd.clear()
    lcd.message = "Testing..."
    time.sleep(2)
    lcd.clear()
    # message to be scrolled
    scroll_msg = "Done! Turning Off"
    lcd.message = scroll_msg
    # scrolling message
    for i in range(len(scroll_msg)):
        time.sleep(1)
        lcd.move_left()
    time.sleep(1)
    lcd.clear()
