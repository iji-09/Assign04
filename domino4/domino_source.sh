#!/usr/bin/bash

pins=(14 15 20 21)

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

while true; do
    for pin in "${pins[@]}"; do
        # LED 켜기
        pinctrl set $pin dh
        sleep 1
        
        # LED 끄기 (다음 LED를 켜기 위해)
        pinctrl set $pin dl
    done
done
