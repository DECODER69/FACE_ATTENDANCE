import serial
import time


ser = serial.Serial("COM3", 9600, timeout=1)

data = bytes.fromhex('FF 01 01')
ser.write(data)
time.sleep(2)

data2 = bytes.fromhex('FF 01 00')
ser.write(data2)
time.sleep(2)

ser.close()