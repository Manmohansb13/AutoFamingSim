from flask import Flask, render_template, request
import serial

app = Flask(__name__)

ser = serial.Serial('COM8', 9600)  # Replace 'COM3' with your Arduino's serial port

@app.route('/')
def index():
    data = ser.readline().decode('utf-8').strip()
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
