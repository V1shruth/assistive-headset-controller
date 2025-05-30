# 🎧 Assistive Headset Controller — Cheek Sensor-Based Input for Children

This project turns a simple cheek movement into keyboard input (like `ENTER` or `TAB`) for children with limited mobility. It uses a QT Py RP2040 board and a VCNL4040 proximity sensor to simulate keystrokes based on subtle facial gestures.

🛠 Designed to be easy-to-use by **teachers**, **therapists**, and **non-programmers** — just plug it in and go.

---

## 📦 What's Included

- `code.py`: The main program. This runs automatically when the board is powered on.
- `README.md`: This guide.

---

## 🧰 What You Need

| Item                          | Purpose                                      | Example |
|------------------------------|----------------------------------------------|---------|
| QT Py RP2040 (by Adafruit)   | Small, programmable microcontroller          | [Buy](https://www.adafruit.com/product/4900) |
| VCNL4040 Sensor              | Detects cheek proximity (movement)           | [Buy](https://www.adafruit.com/product/4666) |
| STEMMA QT Cable              | Easily connects sensor to board              | [Buy](https://www.adafruit.com/product/4210) |
| USB-C Cable                  | Powers board and sends keystrokes            | —       |
| Computer (Mac, PC, etc.)     | For testing and using the input              | —       |
| Headset or boom mount        | To hold sensor next to the child’s cheek     | —       |

---

## 🧠 How It Works

- ✅ **Single cheek jab** → triggers `ENTER` key
- ✅ **Double cheek jab (within 0.75 seconds)** → triggers `TAB` key

This allows the child to **submit** or **move between form fields**, using only a cheek gesture.

---

## 🔧 Setup Instructions

### 1. Install CircuitPython on the Board
1. Go to: [circuitpython.org/board/qtpy_rp2040](https://circuitpython.org/board/qtpy_rp2040)
2. Download the latest `.uf2` file
3. Plug in the QT Py RP2040
4. **Double-tap the reset button** (it will show up as `RPI-RP2`)
5. Drag the `.uf2` file into `RPI-RP2`
6. It will reboot and appear as a USB drive called `CIRCUITPY`

---

### 2. Install the Code
1. Open the `CIRCUITPY` drive
2. Delete any old `code.py` file
3. Copy this repo’s `code.py` into it
4. That’s it — the code runs automatically!

---

## 🧪 How to Test It (Optional)

To see what the sensor is detecting, open the Serial Monitor:

### ▶️ On Mac/Linux
1. Open Terminal
2. Type:
   ```bash
   ls /dev/tty.usbmodem*

3. Then:
    ```bash
    screen /dev/tty.usbmodemXXXX 115200
(replace XXXX with your device number)

4. You'll see logs like: 
    ```bash
    Proximity: 103
    Object approaching...
    Tapped: ENTER pressed

To exit:
Ctrl+A then Ctrl+\, then press Y

▶️ On Windows
Download Mu Editor

Select "CircuitPython" mode

Click Serial — you’ll see the same log output

