import serial
import time

# Configure the serial port
ser = serial.Serial('/dev/ttyUSB0', 9600)  # Replace '/dev/ttyUSB0' with the appropriate port for your Zeebee dongle
ser.timeout = 1  # Set timeout to 1 second

# Function to send data to the Zigbee device
def send_command(command):
    ser.write(command.encode())
    time.sleep(0.1)  # Wait for the device to respond
    response = ser.read_all().decode()
    return response

# Example command to send to the Zigbee device
command = "AT\r\n"

# Send the command and print the response
response = send_command(command)
print("Response:", response)

# Close the serial port when done
ser.close()
