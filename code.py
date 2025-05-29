import board
import busio
import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
import adafruit_vcnl4040

# Initialize I2C
i2c = busio.I2C(board.SCL1, board.SDA1)

# Initialize sensor
vcnl4040 = adafruit_vcnl4040.VCNL4040(i2c)

# Keyboard HID
keyboard = Keyboard(usb_hid.devices)

# Sensitivity threshold
JAB_THRESHOLD = 15  # change this if needed
DEBOUNCE_TIME = 0.2
DOUBLE_JAB_WINDOW = 0.75

# State tracking
last_proximity = vcnl4040.proximity
last_jab_time = None
pending_enter = False
pending_enter_time = None

def press_key(key):
    keyboard.press(key)
    time.sleep(0.1)
    keyboard.release(key)

print("System Ready.")

while True:
    try:
        current_proximity = vcnl4040.proximity
        diff = current_proximity - last_proximity
        now = time.monotonic()

        print(f"Proximity: {current_proximity}")

        # Detect Jab (sharp increase in proximity)
        if diff > JAB_THRESHOLD:
            print("Object approaching...")

            if pending_enter:
                # Second jab within double jab window → register as TAB
                if now - pending_enter_time <= DOUBLE_JAB_WINDOW:
                    print("Double jab detected — TAB pressed")
                    press_key(Keycode.TAB)
                    pending_enter = False
                    last_jab_time = None
                    pending_enter_time = None
                else:
                    # Too late — fallback, ENTER will trigger shortly
                    print("Second jab too late. Waiting to resolve ENTER...")
            else:
                # First jab detected — don't press ENTER yet, wait to see if a second one comes
                pending_enter = True
                pending_enter_time = now
                print("First jab detected — waiting for possible second...")

            time.sleep(DEBOUNCE_TIME)  # debounce

        # If enough time passed and second jab didn't come — trigger ENTER
        if pending_enter and (now - pending_enter_time > DOUBLE_JAB_WINDOW):
            print("Single jab confirmed — ENTER pressed")
            press_key(Keycode.ENTER)
            pending_enter = False
            pending_enter_time = None
            last_jab_time = None

        last_proximity = current_proximity
        time.sleep(0.05)

    except OSError as e:
        print("Sensor error:", e)
