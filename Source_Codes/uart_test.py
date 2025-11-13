import serial
import time

ser = serial.Serial("/dev/serial0", 115200, timeout=1)
time.sleep(2)  # Let UART stabilize

count = 0

while True:
    msg = f"Ping {count}\n"
    ser.write(msg.encode())
    print(f"[Pi  ^f^r ESP32] {msg.strip()}")

    time.sleep(0.5)  # Wait before reading

    if ser.in_waiting:
        response = ser.readline().decode().strip()
        print(f"[ESP32  ^f^r Pi] {response}")

    count += 1
    time.sleep(1)






