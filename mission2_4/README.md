
---

## 미션 2-4

이 프로젝트는 Raspberry Pi에서 **버튼을 누를 때마다 숫자를 1씩 증가시켜**,  
그 숫자를 **4개의 LED에 2진수로 표시**하는 프로그램입니다.  
`gpiozero` 라이브러리를 사용해 간단한 인터페이스로 GPIO 핀을 제어합니다.

---

## 코드 설명

```python
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
```

---

## 주요 구성 요소 설명

- **`LED(pin)`**: 각 GPIO 핀에 연결된 LED를 제어하는 객체입니다.
- **`Button(25)`**: GPIO 25번에 연결된 버튼 입력을 감지합니다.
- **`leds` 리스트**: GPIO 8, 7, 16, 20번에 연결된 LED를 리스트로 관리합니다.
- **`count` 변수**: 버튼을 누를 때마다 증가하며 현재 상태(숫자)를 저장합니다. 0부터 15까지만 표현 (4비트).
- **`show_binary()` 함수**:
  - 버튼을 누를 때마다 `count` 값을 1 증가시키고, 16이 되면 다시 0으로 돌아갑니다.
  - 이 숫자를 **2진수로 변환한 후**, 각 비트를 LED에 출력합니다.
    - 예: `count == 6` → 2진수 `0110` → LED2, LED3만 켜짐
- **`pause()`**: 프로그램을 계속 대기시켜 버튼 입력을 감지할 수 있도록 유지합니다.
- **`KeyboardInterrupt 처리`**: `Ctrl+C`로 종료 시 `"종료됨"` 메시지를 출력합니다.

---

## 연결 구성

| 구성 요소 | GPIO 핀 번호 |
|------------|--------------|
| 버튼       | GPIO 25번 (입력) |
| LED 1 (LSB) | GPIO 8번 |
| LED 2      | GPIO 7번 |
| LED 3      | GPIO 16번 |
| LED 4 (MSB) | GPIO 20번 |

> **LSB (Least Significant Bit)** → GPIO 8  
> **MSB (Most Significant Bit)** → GPIO 20

※ `gpiozero.Button`은 기본적으로 내부 풀업 저항을 사용하므로 외부 저항이 필요 없습니다.

---

## 동작 방식

1. 프로그램을 실행하면, 버튼을 누를 때마다 `count` 값이 1씩 증가합니다.
2. 그 값을 **4비트 2진수로 변환하여 LED에 출력**합니다.
   - 예: 0 → `0000`, 1 → `0001`, 2 → `0010`, ..., 15 → `1111`
3. 값이 15를 넘으면 다시 0부터 시작합니다.
4. `Ctrl+C`로 프로그램을 안전하게 종료할 수 있습니다.

---

## 실행 예시

```bash
python3 mission2_binary_counter.py
```

버튼을 반복해서 누르면 LED들이 2진수처럼 점점 바뀌는 걸 볼 수 있습니다.

---

## 예시 출력

| 버튼 누른 횟수 | Count 값 | LED 상태 (GPIO: 20 16 7 8) |
|----------------|-----------|-----------------------------|
| 0 (초기값)     | 0         | 0000                        |
| 1              | 1         | 0001                        |
| 2              | 2         | 0010                        |
| ...            | ...       | ...                         |
| 15             | 15        | 1111                        |
| 16             | 0         | 0000                        |

---

## 파일 구조 예시

```
mission2_binary/
├── mission2_binary_counter.py   ← 2진수 LED 카운터 코드
└── README.md                    ← 코드 설명 파일
```

---

## 참고

- `count >> i & 1`은 현재 숫자를 이진수로 표현했을 때 `i`번째 비트가 1인지 확인하는 방식입니다.
- 이 방식은 **비트 연산에 익숙해지는 연습**에도 매우 유용합니다.
