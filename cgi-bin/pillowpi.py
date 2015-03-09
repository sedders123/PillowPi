#!/usr/bin/env python

import cgi
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

GPIO.setup(23, GPIO.IN) # Light
GPIO.setup(24, GPIO.IN) # Temp
GPIO.setup(6, GPIO.IN) # Butt_0
GPIO.setup(5, GPIO.IN) # Butt_1

light = "OK"
temp =  "OK"

def http_header():
        '''generates http header'''
        print("Content-type:text/html\n")
def html_top():
        '''produces top and head section of the web page to be generated'''
        print(""" 
	<!DOCTYPE html>
	<html lang="en">
	<head>
	<title>My Page</title>
	</head>
	<body>
	""")


def html_bottom():
        '''generates closing tags for the end of the web page'''
        print("""
	</body>
	</html>
	""")
        
def main():
    global light,temp
    
    if GPIO.input(23) == True:
        light = "HIGH"
    else:
        light = "OK"

    if GPIO.input(24) == True:
        temp = "HIGH"
    else:
        temp = "OK"
        
    print("Light: {}".format(light))
    print("Temperature: {}".format(temp))
    
while __name__=="__main__":
        http_header()
        html_top()
        main()
        html_bottom()
        sleep(5)
	
	
