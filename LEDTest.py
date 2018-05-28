import serial
#python -m serial.tools.list_ports
ser = serial.Serial('COM1', 9600, timeout = 1)
print(ser.name)
print ("Done")
while True:
    b = ser.read().decode()
    print(b)
