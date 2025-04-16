from gpiozero import LED, Button
from signal import pause

button = Button(25)
leds = [LED(pin) for pin in [8, 7, 16, 20]]

def turn_on():
    for led in leds:
        led.on()

def turn_off():
    for led in leds:
        led.off()

button.when_pressed = turn_on
button.when_released = turn_off

try:
    pause()
except KeyboardInterrupt:
    print("사용자에 의해 종료됨")
