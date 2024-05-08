#!/usr/bin/python3
import os
import datetime
from sense_hat import SenseHat

file_name = datetime.date.today()
file_path = "/etc/docker/" + str(file_name) + ".txt"

sense = SenseHat()
sense.clear()
temp_C = round(sense.get_temperature())
# temp_F = (9*temp_C)/5+32

hour = datetime.datetime.now().hour
minute = datetime.datetime.now().minute

time = str(hour) + "h" + str(minute) + "m: "
current_Temp = str(temp_C) + "C\n"

if os.path.exists(file_path):
	with open (file_path, 'a') as fp:
 		fp.write(time + current_Temp)
else:
 	with open(file_path, 'w') as fp:
 		fp.write(time + current_Temp)
