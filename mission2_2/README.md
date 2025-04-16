

## 버튼 눌림에 따라 LED 상태 토글

```markdown
# Toggle LEDs with Button (Raspberry Pi + gpiozero)

이 프로젝트는 Raspberry Pi에서 버튼을 눌렀을 때 **여러 개의 LED의 상태(ON/OFF)를 전환(toggle)** 하는 프로그램입니다.  
`gpiozero` 라이브러리를 이용하여 GPIO 핀에 연결된 LED와 버튼을 간편하게 제어할 수 있습니다.

---

## 코드 설명

```python
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
```

---

## 주요 구성 요소 설명

- **`LED(pin)`**: 지정한 GPIO 핀 번호에 연결된 LED 객체를 생성합니다.
- **`Button(25)`**: GPIO 25번에 연결된 버튼을 감지합니다.
- **`leds` 리스트**: 4개의 LED(GPIO 8, 7, 16, 20번)가 리스트에 저장되어 제어됩니다.
- **`led_state` 변수**: 현재 LED가 켜졌는지 꺼졌는지 상태를 저장하는 불리언 값입니다.
- **`toggle_leds()` 함수**:
  - 버튼이 눌릴 때마다 실행되며, `led_state` 값에 따라 LED를 켜거나 끕니다.
  - LED 상태를 반대로 전환하고 `led_state`를 갱신합니다.
- **`button.when_pressed`**: 버튼이 눌렸을 때 `toggle_leds()` 함수를 호출하도록 연결합니다.
- **`pause()`**: 프로그램이 종료되지 않도록 대기합니다.
- **`KeyboardInterrupt 처리`**: `Ctrl+C`로 프로그램을 종료할 때 메시지를 출력합니다.

---

## 연결 구성

| 구성 요소 | GPIO 핀 번호 |
|------------|--------------|
| 버튼       | GPIO 25번 (입력) |
| LED 1      | GPIO 8번 |
| LED 2      | GPIO 7번 |
| LED 3      | GPIO 16번 |
| LED 4      | GPIO 20번 |

※ 버튼은 내부 풀업 저항 기능이 자동으로 활성화되므로, 외부 풀업 저항 없이 사용할 수 있습니다.

---

## 동작 흐름

1. 프로그램 실행 후, 버튼을 **한 번 누르면** 4개의 LED가 **모두 켜짐**
2. 버튼을 **다시 누르면** 4개의 LED가 **모두 꺼짐**
3. 이 동작을 반복하여 LED 상태가 **토글**됨
4. `Ctrl+C`를 눌러 프로그램을 안전하게 종료 가능

---

## 실행 예시

```bash
python3 mission2_toggle.py
```

버튼을 누를 때마다 LED의 상태가 바뀌는 것을 실시간으로 확인할 수 있습니다.

---

## 파일 구조 예시

```
mission2_toggle/
├── mission2_toggle.py     ← 토글 제어 코드
└── README.md              ← 코드 설명 파일
```

```
