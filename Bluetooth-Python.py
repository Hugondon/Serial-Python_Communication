import time

import serial

# https://www.youtube.com/watch?v=3tcn496oxnk
# https://superuser.com/questions/1237268/
print("Start")
port = "COM8"
baudrate = 9600
bluetooth = serial.Serial(port, 9600)
print("Connected")
bluetooth.flushInput()  # ?
for i in range(5):
    print("Ping")
    bluetooth.write(b"BOOP " + str.encode(str(i)))  # Numerically incremented ping
    input_data = bluetooth.readline()
    print(input_data.decode())  # There are bytes coming in so a decode is needed
    time.sleep(0.1)
bluetooth.close()  # Otherwise the connection will remain open until a timeout which ties up the COM Port
print("Done")
