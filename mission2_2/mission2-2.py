from gpiozero import LED, Button
from signal import pause

button = Button(25)
leds = [LED(pin) for pin in [8, 7, 16, 20]]

# 현재 LED 상태 저장용 변수
led_state = False

# 버튼 눌릴 때마다 전체 LED 상태 토글
def toggle_leds():
    global led_state
    for led in leds:
        led.on() if not led_state else led.off()
    led_state = not led_state

button.when_pressed = toggle_leds

try:
    pause()
except KeyboardInterrupt:
    print("종료됨")
