from flask import Flask, request
import serial

ser = serial.Serial("/dev/serial0", 115200, timeout=1)

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
    <head>
        <title>ESP32 Robot Control</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                text-align: center;
                margin-top: 50px;
                background-color: #f4f4f9;
            }
            h1 {
                color: #333;
            }
            button {
                width: 120px;
                height: 120px;
                font-size: 22px;
                margin: 15px;
                border-radius: 15px;
                border: none;
                background-color: #4CAF50;
                color: white;
                cursor: pointer;
                box-shadow: 0px 4px 6px rgba(0,0,0,0.2);
                user-select: none;
                -webkit-user-select: none;
            }
            button:active {
                background-color: #45a049;
            }
            .controls {
                display: grid;
                grid-template-columns: 1fr 1fr 1fr;
                gap: 20px;
                max-width: 400px;
                margin: auto;
            }
            .controls div {
                text-align: center;
            }
        </style>
    </head>
    <body>
        <h1>ESP32 Robot Control</h1>
        <div class="controls">
            <div></div>
            <div><button id="forward">Forward</button></div>
            <div></div>

from flask import Flask, request
