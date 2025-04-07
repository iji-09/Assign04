#!/usr/bin/bash

pins=(14 15 20)

# 프로그램 종료 시 모든 LED 끄기
cleanup() {
    for pin in "${pins[@]}"; do
        pinctrl set $pin dl  # 모든 LED 끄기
    done
    echo "All LEDs turned off. Exiting."
    exit 0
}

# Ctrl+C (SIGINT) 시 cleanup 함수 실행
trap cleanup SIGINT

# 숫자를 2진수로 LED에 표시하는 함수
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

# 메인 루프: 0부터 7까지 반복
while true; do
    for num in {0..7}; do
        display_number $num
        sleep 1  # 1초 동안 LED 상태 유지
    done
done
