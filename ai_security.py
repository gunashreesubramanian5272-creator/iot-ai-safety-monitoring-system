import serial
import time
from firebase_setup import send_data

# -----------------------------
# RULE-BASED AI FUNCTION
# -----------------------------
def check_status(temp, water, current):
    if temp > 80:
        return "HIGH TEMP ALERT"
    elif water < 30:
        return "LOW WATER ALERT"
    elif current > 90:
        return "HIGH CURRENT ALERT"
    else:
        return "SAFE"

# -----------------------------
# ARDUINO CONNECTION
# -----------------------------
ser = serial.Serial('COM16', 9600)

print("System Started...")

while True:
    try:
        data = ser.readline().decode(errors='ignore').strip()
        print("Sensor:", data)

        # -----------------------------
        # SAFE PARSING BLOCK
        # -----------------------------
        parts = data.split("|")

        temp = None
        water = None
        current = None

        for p in parts:
            try:
                key, value = p.split(":")
                key = key.strip().lower()
                value = int(value.strip())

                if "temp" in key:
                    temp = value
                elif "water" in key:
                    water = value
                elif "current" in key:
                    current = value

            except:
                continue

        # Skip bad data
        if temp is None or water is None or current is None:
            print("Bad sensor data skipped")
            continue

        # -----------------------------
        # RULE-BASED ANALYSIS
        # -----------------------------
        status = check_status(temp, water, current)

        print("System Status:", status)

        # -----------------------------
        # SEND TO FIREBASE
        # -----------------------------
        send_data(temp, water, current, status)

        print("Sent to Firebase ✔")

    except Exception as e:
        print("Error:", e)

    time.sleep(2)
