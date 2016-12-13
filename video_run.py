#!/usr/bin/env python

import os
import subprocess
import RPi.GPIO as GPIO
import time

input_pin=25
output_pin=7
myfile1="playvideo.mp4"
mypathlist=["/media","/mnt"]
file1_path=""

GPIO.setmode(GPIO.BCM)
GPIO.setup(input_pin,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
#GPIO.setup(output_pin,GPIO.OUT)

# Go screen black
black_screen_pid=subprocess.Popen("fbi -a -T 1 -v -noverbose /home/pi/raspi_progs/video_test/Vending_Flipped.jpg &",shell=True)

#print black_screen_pid

def find(name, path):
	for root, dirs, files in os.walk(path):
 		if name in files:
			return os.path.join(root, name)
		
	
proc1_exists=0
proc2_exists=0
flag=0
bounce_delay=0.2

def search_file(mypath):
	global file1_path
	file1_path=find(myfile1,mypath)
	#file2_path=find(myfile2,mypath)
	#
	#print file1_path
	#print file2_path

	#if file1_path and file2_path:
	if file1_path :
		#GPIO.output(output_pin,GPIO.HIGH)
		return 1
		#break
	else:
		#GPIO.output(output_pin,not(GPIO.input(output_pin)))
		#time.sleep(0.2)
		pass



def file_exists():
	for mypath in mypathlist:
		#print mypath
		x=search_file(mypath)
		#print x
		if x:
			return 1
		else:
			subprocess.call("mount -a 2> /dev/null",shell=True)
while True:
	#print "in file exists"
	exists_flag=file_exists()
	if exists_flag==1:
		break

cmd1="omxplayer --loop --no-osd %s" %file1_path
#cmd2="omxplayer %s" %file2_path
cmd2="ls > /dev/null"


def main():
	global proc1_exists
	global proc2_exists
	global flag
	#while True:
	#	print "in main"

	#print cmd1
	#print cmd2

	#raw_input()
	#print "entering while"
	
	while True:
        	x=GPIO.input(input_pin)
		file_exists()
		#print "in Main Loop - ",x
		if x == 1:
			#time.sleep(bounce_delay)	
            		x=GPIO.input(input_pin)
			if x==1:
				flag=0
				subprocess.call("killall -9 omxplayer.bin",shell=True)
				subprocess.call("killall -9 omxplayer",shell=True)
        	elif x==0 :
            		#time.sleep(bounce_delay)
			x=GPIO.input(input_pin)
			if x==0 and flag==0:
           			proc2=subprocess.Popen("exec "+ cmd1, shell=True)
				flag=1

if __name__== "__main__":
	main()
