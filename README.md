# ESP32-Raspberry-Pi-2W-Remote-Bot-Control
This project provides a simple web interface to control  motot-driven robot connected to a Raspberry Pi.
The communication between the web server and the motor driver happens through UART using Python.

The interface is built using Flask, and you can control the bot through buttons on a webpage.
The project is intended for local network control.

![WhatsApp Image 2025-11-30 at 17 36 49_c4515a21](https://github.com/user-attachments/assets/de3565ee-f0bb-46df-b9ff-3298a6dd5ee6)


## Hardware Used
- Raspberry Pi (Python Flask Web Server)

- ESP32 (Motor Driver Control using UART)

- L298N Motor Driver

- Web UI (Forward, Back, Left, Right controls)

The project works inside your local Wi-Fi network and can be accessed from:

- Mobile/PC phone browser

- SSH terminal (for starting Flask server)

## Software Dependencies
Install required packages:
```sh
sudo apt update
sudo apt install python3 python3-pip
pip3 install -r requirements.txt
```
Enable ssh for Raspberry Pi
```sh
sudo raspi-config
```
<img width="1107" height="403" alt="image" src="https://github.com/user-attachments/assets/12313928-235c-4e54-9b32-40c83e0d5139" />

Interface Options -> I1 SSH -> Enable

Commaands to check the GPIO pins & board details
```sh
pintest
ps aux | grep python
pinout
```
Commuite to your project folder
Create a Virtual environment for the folder name venv
- keeps the Python project library isolated
- Avoid messing with systems built in python
```sh
python3 -m venv venv
```
Switch terminal to use virtual environment (while running the project)
```sh
source venv/bin/activate
```
Program Esp32 with the motor driver
create directory and run the code  in Pi
```sh
nano interface_code.py
python interface_code.py
(venv) Pi@raspi:~/esp_bot $ python robot_server.py 
 * Serving Flask app 'interface_code'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:8080
 * Running on http://192.1x8.0.1x0:8080
```
<img width="1509" height="604" alt="{D5275583-3820-4D74-B8F1-101937BAB4CB}" src="https://github.com/user-attachments/assets/e525af51-f476-40b7-8577-c0a01917044d" />

## Note
- This project is ment for local useage only.
- No tunneling was used
- Learning Flask + UART + Raspberry Pi basics
