
## 미션 2-1

### 구현 영상
https://youtu.be/mOjALKbTfr0


```markdown
# Button-Controlled LED Lighting System (Raspberry Pi + gpiozero)

이 프로젝트는 Raspberry Pi의 GPIO 핀을 사용하여, **버튼을 누르면 여러 개의 LED가 켜지고**, 버튼에서 손을 떼면 **LED가 꺼지도록** 제어하는 간단한 회로 제어 프로그램입니다. `gpiozero` 라이브러리를 사용하여 작성되었습니다.

---

## 코드 설명

```python
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
```

### 주요 구성 요소

- **`LED(pin)`**: GPIO 번호를 받아 해당 핀에 연결된 LED를 제어합니다.
- **`Button(25)`**: GPIO 25번 핀에 연결된 버튼 입력을 감지합니다.
- **`leds` 리스트**: 4개의 LED가 각각 GPIO 8, 7, 16, 20번에 연결되어 있어 리스트로 관리됩니다.
- **`turn_on()` 함수**: 버튼이 눌리면 리스트의 모든 LED를 `on()` 합니다.
- **`turn_off()` 함수**: 버튼에서 손을 떼면 모든 LED를 `off()` 합니다.
- **`button.when_pressed` / `when_released`**: 버튼 이벤트(눌림 / 뗌)에 따라 함수가 자동 실행됩니다.
- **`pause()`**: 프로그램이 종료되지 않고 계속 실행되도록 유지합니다.
- **`try / except KeyboardInterrupt`**: 사용자가 `Ctrl+C`로 종료할 경우 친절한 메시지를 출력합니다.


---

## 연결 방법

| 구성 요소 | GPIO 핀 번호 |
|------------|--------------|
| 버튼       | GPIO 25번 (입력) |
| LED 1      | GPIO 8번 |
| LED 2      | GPIO 7번 |
| LED 3      | GPIO 16번 |
| LED 4      | GPIO 20번 |

**버튼은 풀업 저항 방식**으로 동작하며, `gpiozero.Button`은 내부 풀업(Pull-Up)을 기본 사용하므로 외부 저항이 없어도 됩니다.

---

## 동작 방식

1. 버튼을 **누르면**, 모든 LED가 **켜진다**.
2. 버튼에서 **손을 떼면**, 모든 LED가 **꺼진다**.
3. 프로그램은 `pause()`로 **계속 대기**하며 동작을 유지한다.
4. `Ctrl+C`로 종료하면 `"사용자에 의해 종료됨"` 메시지가 출력된다.
