#Use this command to install pynetworktables "pip install pynetworktables"
from networktables import NetworkTables
#Use this command to install pySerial "pip install pyserial"
import serial
import time
import logging
#python -m serial.tools.list_ports (run this command in command line to list Ports)
#On Windows ports will look like COM3, Linux will look like /dev/ttyUSB0
ser = serial.Serial('COM3', 9600, timeout = 1)
#Confirms Serial was set up properly
print(ser.name)
#Allows you to receive NetworkTables messages
logging.basicConfig(level=logging.DEBUG)
#Set up an instance of NetworkTables using the default one that is created
inst = NetworkTables.getDefault()
#Access the table named "operator"
operatorTable = inst.getTable("operator")
#Access the entry name "gotCube"
gotCubeEntry = operatorTable.getEntry("gotCube")
#Start NetworkTables Server at Specified IP, IP can be found by looking in a SmartDashboard Window and looking at the IP listed at the top
NetworkTables.initialize(server='10.40.26.100')
#Sleep to allow Server to start and connect
time.sleep(3)
#Loop to keep updating values as long as script is running
while True:
	#Retrieve value from entry
	gotCube = gotCubeEntry.getBoolean(False)
	#Print value from entry
	print(gotCube)
	#if gotCube is True write '1' to Serial for the Arduino to read, else write '0' to Serial for the Arduino
	if gotCube:
		ser.write(b'1')
		print("1")
		#Sleep to not overload Arduino with data. This can be tweaked for optimal performance but I have found that .09 keeps the Arduino pretty well fed with data with not too much lag between changing
		time.sleep(.09)
	else:
		ser.write(b'0')
		print("0")
		#Sleep to not overload Arduino with data. This can be tweaked for optimal performance but I have found that .09 keeps the Arduino pretty well fed with data with not too much lag between changing
		time.sleep(.09)
