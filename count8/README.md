

## LED 3비트 카운터 

### 📺 카운터 구현 영상
<a href="https://youtu.be/cY8pAI3HAAY">
    <img src="https://img.youtube.com/vi/cY8pAI3HAAY/0.jpg" alt="YouTube 영상" width="600">
</a>

---

### 개요
이 Bash 스크립트는 3개의 LED를 사용하여 **0부터 7까지의 숫자를 2진수로 표현하는 LED 카운터**를 구현합니다.  
LED는 0부터 7까지의 숫자를 1초 간격으로 순차적으로 표시하며 무한히 반복합니다.  
또한, 프로그램 종료 시 모든 LED를 안전하게 끄도록 설정하였습니다.  

---

### 사용 방법

1. **스크립트 실행 권한 부여**
   ```bash
   chmod +x ~/bin/count8
   ```
   
2. **스크립트 실행**
   ```bash
   ~/bin/count8
   ```
   
3. **프로그램 종료**
   - `Ctrl+C`를 눌러 프로그램을 종료할 수 있습니다.  
   - 종료 시 모든 LED가 안전하게 꺼집니다.  

---

### 코드 설명

#### 1. 핀 번호 배열 설정
```bash
pins=(14 15 20)
```
- LED가 연결된 GPIO 핀 번호를 배열로 지정합니다.  
- **14번 핀**: LSB (Least Significant Bit, 2⁰)  
- **15번 핀**: 중간 비트 (2¹)  
- **20번 핀**: MSB (Most Significant Bit, 2²)  

---

#### 2. 종료 처리 함수 (`cleanup()`)
```bash
cleanup() {
    for pin in "${pins[@]}"; do
        pinctrl set $pin dl  # 모든 LED 끄기
    done
    echo "All LEDs turned off. Exiting."
    exit 0
}
```
- 프로그램이 종료될 때 모든 LED를 끄는 함수입니다.  
- `trap` 명령어와 함께 사용하여 `Ctrl+C`로 종료할 때도 안전하게 LED를 끕니다.  

---

#### 3. 종료 시그널 트랩 설정
```bash
trap cleanup SIGINT
```
- `SIGINT` 신호 발생 시(`Ctrl+C`) `cleanup()` 함수를 실행하여 모든 LED를 끕니다.  

---

#### 4. 숫자를 LED로 표시하는 함수 (`display_number()`)
```bash
display_number() {
    local num=$1
    local binary=$(printf "%03d" "$(echo "obase=2; $num" | bc)")

    for i in {0..2}; do
        if [ "${binary:$((2 - i)):1}" -eq "1" ]; then
            pinctrl set ${pins[$i]} dh   # LED 켜기
        else
            pinctrl set ${pins[$i]} dl   # LED 끄기
        fi
    done
}
```
- 입력받은 숫자를 3비트로 변환하여 LED에 표시합니다.  
- 예를 들어, 숫자 `5`는 `101`로 변환되어 **20번 핀(MSB)와 14번 핀(LSB)**이 켜집니다.  

---

#### 5. 메인 루프
```bash
while true; do
    for num in {0..7}; do
        display_number $num
        sleep 1  # 1초 동안 LED 상태 유지
    done
done
```
- 0부터 7까지의 숫자를 1초 간격으로 순차적으로 표시하고, 계속 반복합니다.  

---

### 구현 동작
1. 숫자 `0` → `000` (모든 LED 꺼짐)  
2. 숫자 `1` → `001` (14번 LED 켜짐)  
3. 숫자 `2` → `010` (15번 LED 켜짐)  
4. 숫자 `3` → `011` (14번 LED, 15번 LED 켜짐)  
5. 숫자 `4` → `100` (20번 LED 켜짐)  
6. 숫자 `5` → `101` (14번 LED, 20번 LED 켜짐)  
7. 숫자 `6` → `110` (15번 LED, 20번 LED 켜짐)  
8. 숫자 `7` → `111` (모든 LED 켜짐)  

---

### 문제 해결
- `Ctrl+C`로 강제 종료했을 때 LED가 켜져 있는 문제가 발생할 수 있습니다.  
  - 이를 해결하기 위해 `cleanup()` 함수와 `trap` 명령어를 사용하여 프로그램 종료 시 모든 LED를 끄도록 설정하였습니다.  

---

### 회로 구현 이미지
![KakaoTalk_20250407_144241769](https://github.com/user-attachments/assets/4cac8fdd-ddbd-491f-a3f0-66870da2faa2)

---
