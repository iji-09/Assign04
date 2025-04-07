---

## LED 도미노 구현

### 개요
이 Bash 스크립트는 4개의 LED를 순서대로 켜고 끄는 **LED 도미노 효과**를 구현합니다.  
LED는 순차적으로 켜졌다가 꺼지며, 이 동작을 무한히 반복합니다.  
또한, 프로그램 종료 시 모든 LED를 안전하게 끄도록 처리되어 있습니다.  

---

### 사용 방법

1. **스크립트 실행 권한 부여**
   ```bash
   chmod +x ~/bin/domino4
   ```
   
2. **스크립트 실행**
   ```bash
   ~/bin/domino4
   ```
   
3. **프로그램 종료**
   - `Ctrl+C`를 눌러 프로그램을 종료할 수 있습니다.  
   - 종료 시 모든 LED가 안전하게 꺼집니다.  

---

### 코드 설명

#### 1. 핀 번호 배열 설정
```bash
pins=(14 15 20 21)
```
LED가 연결된 GPIO 핀 번호를 배열로 지정합니다.  
- 14번 핀, 15번 핀, 20번 핀, 21번 핀을 사용하여 4개의 LED를 제어합니다.  

---

#### 2. 종료 처리 함수 (`cleanup`)
```bash
cleanup() {
    for pin in "${pins[@]}"; do
        pinctrl set $pin dl
    done
    echo "All LEDs turned off. Exiting."
    exit 0
}
```
- 프로그램이 종료될 때 모든 LED를 끄는 함수입니다.  
- `trap` 명령어와 함께 사용하여 `Ctrl+C`로 종료할 때도 안전하게 LED를 끌 수 있습니다.  

---

#### 3. 종료 시그널 트랩 설정
```bash
trap cleanup SIGINT
```
- `SIGINT` 신호가 발생할 때(즉, `Ctrl+C` 입력 시) `cleanup` 함수를 호출합니다.  
- 이를 통해 강제 종료 시에도 모든 LED를 안전하게 끌 수 있습니다.  

---

#### 4. LED 점등 루프
```bash
while true; do
    for pin in "${pins[@]}"; do
        pinctrl set $pin dh  # LED 켜기
        sleep 1               # 1초 대기
        pinctrl set $pin dl  # LED 끄기
    done
done
```
- 무한 루프를 이용하여 LED를 반복적으로 켜고 끕니다.  
- 각 LED는 1초 동안 켜졌다가 다음 LED로 넘어갑니다.  
- 모든 LED가 켜졌다 꺼지면 처음 LED로 다시 돌아갑니다.  

---

### 구현 동작
1. LED 14 켜짐 → 1초 대기 → LED 14 꺼짐  
2. LED 15 켜짐 → 1초 대기 → LED 15 꺼짐  
3. LED 20 켜짐 → 1초 대기 → LED 20 꺼짐  
4. LED 21 켜짐 → 1초 대기 → LED 21 꺼짐  
5. 처음 LED로 돌아가서 반복  

---

### 문제 해결
- `Ctrl+C`로 강제 종료했을 때 LED가 켜져 있는 문제가 발생할 수 있습니다.  
  - 이 문제를 해결하기 위해 `cleanup()` 함수와 `trap` 명령어를 사용하여 **종료 시 모든 LED를 끄도록 설정**하였습니다.  

---

## 회로 구현 이미지
![KakaoTalk_20250407_144241769](https://github.com/user-attachments/assets/63b4d7b6-6e9a-473f-8922-4666a62c1285)

