import serial
import time


# ser = serial.Serial("COM3", 9600, timeout=1)

# data = bytes.fromhex('FF 01 01')
# ser.write(data)
# time.sleep(2)

# data2 = bytes.fromhex('FF 01 00')
# ser.write(data2)
# time.sleep(2)

# ser.close()

# def send_command_to_ch340(command, port='COM4', baudrate=9600):
#     try:
#         # Open the serial port
#         ser = serial.Serial(port, baudrate)
        
#         # Write the command to the serial port
#         ser.write(command.encode('utf-8'))
        
#         # Close the serial port
#         ser.close()
        
#         return "Command sent successfully."
#     except serial.SerialException as e:
#         return str(e)

# command = "B0"
# # result = send_command_to_ch340(command)
# # print(result)


ser = serial.Serial('COM5', 9600)

# data = ('command = "B0"')
command = "F0"
cmd2 = "F1"
ser.write(command.encode('utf-8'))
time.sleep(0.5)

ser.write(cmd2.encode('utf-8'))


# data2 = bytes.fromhex('FF 01 00')
# ser.write(data2)
# time.sleep(2)

# ser.close()
