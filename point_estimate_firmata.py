#!/usr/bin/env python
import cv2
import numpy as np
import time
import math
import serial
import sys
import signal
from PyMata.pymata import PyMata


# ... initiating Arduino ...
# create a PyMata instance
board = PyMata("/dev/ttyACM0")


# ... Basis definitions for Stepper, servo, analog/digital io ... 

# Servo
def servo(angle) :
  	# send the arduino a firmata reset
	board.reset()
	# servo attached to this pin
	SERVO_MOTOR = 5
	# configure the servo
	board.servo_config(SERVO_MOTOR)
	# move the servo to 'angle' degrees
	board.analog_write(SERVO_MOTOR, angle)

# Stepper
def stepper(N,n,speed):
	# send the arduino a firmata reset
	board.reset()
	# configure the stepper to use pins 9.10,11,12 and specify 'N' steps per revolution
	firmata.stepper_config(N, [12, 11, 10, 9])
	time.sleep(.5)
	# ask Arduino to return the stepper library version number to PyMata
	firmata.stepper_request_library_version()
	time.sleep(.5)
	print("Stepper Library Version",)
	print(firmata.get_stepper_version())
	# move motor #0 'n' steps forward at a speed of 'speed'
	firmata.stepper_step(speed, n)

# Callback function (temp)
def print_analog(data):
   	print "analog read = " + data[3]
	force = data[3]

# digitalWrite()
def digitalWrite(BOARD_LED, val) :
	# Setting pinMode for pin BOARD_LED
	board.set_pin_mode(BOARD_LED, board.OUTPUT, board.DIGITAL)
	# Set the output to val
	board.digital_write(BOARD_LED, val)

# analogRead()
def analogRead() :
	board.set_pin_mode(POTENTIOMETER, board.INPUT, board.ANALOG, print_analog)
# delay()
def delay(num) :
	time.sleep(num)

# handler definition
def signal_handler(sig, frame):
    print('You pressed Ctrl+C!!!!')
    if board is not None:
        board.reset()
    sys.exit(0)

# And throw error if necessary 
signal.signal(signal.SIGINT, signal_handler)


		


# ... Image processing stuff ...
# Start Recording 
cap = cv2.VideoCapture(0)
time.sleep(1)
# HSV values to detect orange colour
h,s,v,counter,l,m = 0,255,213,1,8,8 # Orange 
h0,s0,v0 = 24,207,87  # green
# Daylight
h0,s0,v0 = 32,75,145  # green
h,s,v,counter,l,m = 13,88,222,1,8,8 # Orange 
h1,s1,v1 = 50,96,0

# Masking boundaries...
lower_colour = np.array([h,s,v])
upper_colour = np.array([180,255,255])

lower_colour0 = np.array([h0,s0,v0])
upper_colour0 = np.array([180,255,255])

lower_colour1 = np.array([h1,s1,v1])
upper_colour1 = np.array([180,255,255])

# declarations
centroid_x,centroid_y = 0,0

while(True) : 
	_, frame = cap.read()
	
	# RGB to HSV
	hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
	
	# Calculating mask from hsv
	mask = cv2.inRange(hsv,lower_colour, upper_colour)
	mask0 = cv2.inRange(hsv,lower_colour0, upper_colour0)
	mask1 = cv2.inRange(hsv,lower_colour1, upper_colour1)
	
	
	# Finding contours to find Moments & Centroid
	contours, hierarchy = cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
	contours0, hierarchy0 = cv2.findContours(mask0,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
	contours1, hierarchy1 = cv2.findContours(mask1,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
	cv2.drawContours(mask,contours,-1,(255,255,225),-1)
	cv2.imshow('Thimble', mask)
	
	# Initializing area parameter and its corresponding contour, named 'contour_max'
	area_max = 0
	area_max0 = 0
	area_max1 = 0
	
	###### !!!!Computational Burden!!!! You'll improve this somehow. #######
	for h,cnt in enumerate(contours):
		# Finding area of each contour and picking up the one with max area.
		area = cv2.contourArea(cnt)
		if (area > area_max) :
			area_max = area
			contour_max = cnt
			
			
	for h0,cnt0 in enumerate(contours0):
		# Finding area of each contour and picking up the one with max area.
		area = cv2.contourArea(cnt0)
		if (area > area_max0) :
			area_max0 = area
			contour_max0 = cnt0

	for h1,cnt1 in enumerate(contours1):
		# Finding area of each contour and picking up the one with max area.
		area = cv2.contourArea(cnt1)
		if (area > area_max1) :
			area_max1 = area
			contour_max1 = cnt1
			
	# Finding centroid of that cue.
	
	
	
	M = cv2.moments(contour_max)
	
	past_x,past_y = centroid_x,centroid_y
	centroid_x = int(M['m10']/M['m00'])
	centroid_y = int(M['m01']/M['m00'])
	print (centroid_x,centroid_y)
	
	M0 = cv2.moments(contour_max0)
	
	
	centroid_x0 = int(M0['m10']/M0['m00'])
	centroid_y0 = int(M0['m01']/M0['m00'])


	M1 = cv2.moments(contour_max1)
	
	
	centroid_x1 = int(M1['m10']/M1['m00'])
	centroid_y1 = int(M1['m01']/M1['m00'])
	# difference in X & difference in Y per time period
	dX,dY = -(past_x-centroid_x),-(past_y-centroid_y)
	
	cv2.circle(frame,(centroid_x,centroid_y),10,(0,255,0),-1)
	cv2.imshow('Tracked',frame)
	cv2.circle(frame,(centroid_x0,centroid_y0),10,(255,255,0),-1)
	cv2.imshow('Tracked',frame)
	cv2.circle(frame,(centroid_x1,centroid_y1),10,(0,255,255),-1)
	cv2.imshow('Tracked',frame)
	
	# ...... Next probable coordinate prediction | Kinematic equations ......

	#try:
	#	if (dY !=0) or (dX !=0)
	#		theta = math.atan(dY/dX)
	#except:
	#	theta = 1.57		
	#	print "90' hit point"
	#Xp = centroid_x + (dX*(math.cos(theta)))
	#Yp = centroid_y + (dY*(math.sin(theta)))

	Xp = centroid_x + dX
	Yp = centroid_y + dY
	


	# ... Calculating alpha and beta for motors ... 
	# Alpha, beta equations taken from that research paper
	

	# Realtime r1, r2 estimate from camera point of view 
	r1 = math.sqrt((centroid_x0 - centroid_x1)*(centroid_x0 - centroid_x1) + (centroid_y0 - centroid_y1)*(centroid_y0 - centroid_y1))
	r2 = math.sqrt((centroid_x1 - centroid_x)*(centroid_x1 - centroid_x) + (centroid_y1 - centroid_y)*(centroid_y1 - centroid_y))

	# Shifting a,b origin to stepper motor's from frame's origin 
	a = Xp - centroid_x0
	b = Yp - centroid_y0
	a = float(a)
	b = float(b)
	
	try :
		
		# print ((1/(2*r1*r2))*(a*a + b*b -(r1*r1 + r2*r2)))
		# print ((1/(a*a + b*b)) * ((a*(r1+r2*math.cos(beta)))+ (b*r2*math.sqrt(1- ((math.cos(beta))*(math.cos(beta)))))))
		beta = math.acos((1/(2*r1*r2))*(a*a + b*b -(r1*r1 + r2*r2)))
		alpha = math.acos((1/(a*a + b*b)) * ((a*(r1+r2*math.cos(beta)))+ (b*r2*math.sqrt(1- ((math.cos(beta))*(math.cos(beta)))))))
		print "(a,b,X,Y,alpha,beta)",(a,b,centroid_x-centroid_x0,centroid_y-centroid_y0,alpha*(180/3.14),beta*(180/3.14) )
		
	except :
		print "Alpha/Beta calculation failed, division by zero probably."

	
	
	cv2.imshow('Tracked',frame)


	# ... Write Arduino Sketch here ... 
	fl = 1
	while (True):
		digitalWrite(13,1)
		delay(.2)
		digitalWrite(13,0)
		delay(.2)
		servo(100 + 40*fl)
		delay(1)
		if (fl == 1):
			fl = -1
		else :
			fl = -1

	
	
	
	k = cv2.waitKey(5)
	
	if k == 27:
		break

# After math

# Writes a signature image to disk		
cv2.imwrite("Shoot.png",frame)
# Kills camera instance
cap.release()
cv2.destroyAllWindows()
# Shuts-down Arduino interface cleanly
board.close()
	
