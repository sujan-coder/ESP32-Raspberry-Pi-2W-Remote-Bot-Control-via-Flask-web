# ESP32-Raspberry-Pi-2W-Remote-Bot-Control
This project provides a simple web interface to control  motot-driven robot connected to a Raspberry Pi.
The communication between the web server and the motor driver happens through UART using Python.

The interface is built using Flask, and you can control the bot through buttons on a webpage.
The project is intended for local network control.

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

## Note
- This project is ment for local useage only.
- No tunneling was used
- Learning Flask + UART + Raspberry Pi basics
