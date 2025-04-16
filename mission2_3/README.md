

## 미션 2-3

### 구현 영상 

[![Watch the video](https://img.youtube.com/vi/Vt6WmrtoRjY/0.jpg)](https://youtu.be/Vt6WmrtoRjY)


```markdown
# Domino LED Sequence with Button (Raspberry Pi + gpiozero)

이 프로젝트는 Raspberry Pi에서 버튼을 누르면 **4개의 LED가 순차적으로 켜졌다가 꺼지는 "도미노 효과"**를 연출하는 프로그램입니다.  
`gpiozero` 라이브러리와 `sleep` 함수를 사용하여 타이밍 제어를 간단하게 구현합니다.

---

## 코드 설명

```python
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
```

---

## 주요 구성 요소 설명

- **`LED(pin)`**: 각 GPIO 핀 번호에 연결된 LED를 제어하는 객체입니다.
- **`Button(25)`**: GPIO 25번에 연결된 버튼 입력을 감지합니다.
- **`leds` 리스트**: GPIO 8, 7, 16, 20번에 연결된 LED들을 리스트로 관리합니다.
- **`domino_sequence()` 함수**:
  - 버튼이 눌리면 실행됩니다.
  - 리스트의 LED들을 **하나씩 차례대로 켜고 1초 후 꺼짐** (도미노처럼)
  - `sleep(1)`은 각 LED가 켜지는 시간을 의미합니다.
- **`button.when_pressed`**: 버튼이 눌릴 때 `domino_sequence()` 함수가 실행됩니다.
- **`pause()`**: 프로그램을 종료하지 않고 계속 대기시킵니다.
- **`KeyboardInterrupt 처리`**: `Ctrl+C`로 종료 시 `"종료됨"` 메시지를 출력합니다.

---

## 회로 연결 정보

| 구성 요소 | GPIO 핀 번호 |
|------------|--------------|
| 버튼       | GPIO 25번 (입력) |
| LED 1      | GPIO 8번 |
| LED 2      | GPIO 7번 |
| LED 3      | GPIO 16번 |
| LED 4      | GPIO 20번 |

※ `gpiozero.Button`은 내부 풀업 저항을 사용하므로, 외부 저항이 없어도 동작합니다.

---

## 동작 방식

1. 프로그램 실행 후, 버튼을 누르면
2. LED들이 **왼쪽에서 오른쪽으로** 하나씩 순서대로 켜졌다가 꺼짐
   - 예: LED1 → LED2 → LED3 → LED4 (1초 간격)
3. 프로그램은 `pause()`를 통해 계속 대기하며 버튼 입력을 기다림
4. `Ctrl+C`를 누르면 `"종료됨"` 메시지를 출력하며 종료됨

---

## 실행 예시

```bash
python3 mission2_domino.py
```

버튼을 누를 때마다 LED 도미노 시퀀스를 확인할 수 있습니다.

---

## 파일 구조 예시

```
mission2_domino/
├── mission2_domino.py     ← 도미노 효과 구현 코드
└── README.md              ← 코드 설명 파일
```

---

## 참고

- `sleep()`을 이용한 순차 제어는 간단하지만 블로킹 방식이므로, 더 복잡한 제어가 필요하다면 `asyncio`나 `Thread`를 사용할 수 있습니다.
