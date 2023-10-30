import serial

# Define the serial port and baud rate
ser = serial.Serial('COM8', 9600)  # Replace 'COM3' with your Arduino's serial port

while True:
    try:
        data = ser.readline().decode('utf-8').strip()
        print("Received data: " + data)
    except Exception as e:
        print("Error: " + str(e))
