# Assistive Headset Controller (Cheek Sensor Input)

This project enables children with limited mobility to use facial movements to trigger keyboard inputs (ENTER and TAB) using an Adafruit QT Py RP2040 and a VCNL4040 proximity sensor.

## Features
- Single jab = ENTER
- Double jab within 0.75 seconds = TAB
- Designed for ultra-low mobility input
- Smart delay system for accurate gesture recognition

## Setup
1. Flash [CircuitPython](https://circuitpython.org/board/qtpy_rp2040/) on your QT Py RP2040.
2. Copy `code.py` to your `CIRCUITPY` drive.
3. Connect VCNL4040 via STEMMA QT port.
4. Plug into any computer to emulate keypresses.

## Hardware Used
- Adafruit QT Py RP2040
- VCNL4040 Proximity Sensor
- STEMMA QT cables
- USB-C cable
- Headset boom mount

## License
MIT License

---

Created by Vishruth Anugula 🎓
