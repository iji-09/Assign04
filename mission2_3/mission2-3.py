from gpiozero import LED, Button
from signal import pause
from time import sleep

button = Button(25)
leds = [LED(pin) for pin in [8, 7, 16, 20]]

def domino_sequence():
    for led in leds:
        led.on()
        sleep(1)
        led.off()

button.when_pressed = domino_sequence

try:
    pause()
except KeyboardInterrupt:
    print("종료됨")
