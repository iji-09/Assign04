from gpiozero import LED, Button
from signal import pause
from time import sleep

button = Button(25)
leds = [LED(pin) for pin in [8, 7, 16, 20]]

count = 0

def show_binary():
    global count
    count = (count + 1) % 16
    for i, led in enumerate(leds):
        if (count >> i) & 1:
            led.on()
        else:
            led.off()

button.when_pressed = show_binary

try:
    pause()
except KeyboardInterrupt:
    print("종료됨")
