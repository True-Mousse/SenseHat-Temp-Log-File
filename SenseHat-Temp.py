#!/usr/bin/python3
import os
import datetime
from sense_hat import SenseHat

# Get today's date to use as part of the file name
file_name = datetime.date.today()

# File path where temperature data will be stored
file_path = "/etc/docker/Logs/" + str(file_name) + ".txt"

# Initialize the SenseHat object with the Sense HAT hardware
sense = SenseHat()
sense.clear()

# Current temperature in Celsius from the Sense HAT and rounded
temp_C = round(sense.get_temperature())

# Get the current hour and minute 
hour = datetime.datetime.now().hour
minute = datetime.datetime.now().minute

# Format time as a string (e.g., "13h45m: ")
time = str(hour) + "h" + str(minute) + "m: "

# Convert the current temperature to a string (e.g., "25C\n")
current_Temp = str(temp_C) + "C\n"

# Check if the file already exists
if os.path.exists(file_path):
  # Append the current time and temperature to the existing file
	with open (file_path, 'a') as fp:
 		fp.write(time + current_Temp)
else:
  # Create a new file and write the current time and temperature to it
 	with open(file_path, 'w') as fp:
 		fp.write(time + current_Temp)
