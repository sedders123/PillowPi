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
	<meta charset="utf-8">
  <title>PillowPi - Web Interface!</title>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="">
  <meta name="author" content="">

	<!--link rel="stylesheet/less" href="less/bootstrap.less" type="text/css" /-->
	<!--link rel="stylesheet/less" href="less/responsive.less" type="text/css" /-->
	<!--script src="js/less-1.3.3.min.js"></script-->
	<!--append ‘#!watch’ to the browser URL, then refresh the page. -->
	
	<link href="/css/bootstrap.min.css" rel="stylesheet">
	<link href="/css/style.css" rel="stylesheet">
    <link rel="stylesheet" href="/fonts/font-awesome-4.3.0/css/font-awesome.min.css">

  <!-- HTML5 shim, for IE6-8 support of HTML5 elements -->
  <!--[if lt IE 9]>
    <script src="js/html5shiv.js"></script>
  <![endif]-->

    <!-- Favicon Files --->
    <link rel="apple-touch-icon" sizes="57x57" href="favicons/apple-touch-icon-57x57.png">
    <link rel="apple-touch-icon" sizes="60x60" href="favicons/apple-touch-icon-60x60.png">
    <link rel="apple-touch-icon" sizes="72x72" href="favicons/apple-touch-icon-72x72.png">
    <link rel="apple-touch-icon" sizes="76x76" href="favicons/apple-touch-icon-76x76.png">
    <link rel="apple-touch-icon" sizes="114x114" href="favicons/apple-touch-icon-114x114.png">
    <link rel="apple-touch-icon" sizes="120x120" href="favicons/apple-touch-icon-120x120.png">
    <link rel="apple-touch-icon" sizes="144x144" href="favicons/apple-touch-icon-144x144.png">
    <link rel="apple-touch-icon" sizes="152x152" href="favicons/apple-touch-icon-152x152.png">
    <link rel="apple-touch-icon" sizes="180x180" href="favicons/apple-touch-icon-180x180.png">
    <link rel="icon" type="image/png" href="favicons/favicon-32x32.png" sizes="32x32">
    <link rel="icon" type="image/png" href="favicons/android-chrome-192x192.png" sizes="192x192">
    <link rel="icon" type="image/png" href="favicons/favicon-96x96.png" sizes="96x96">
    <link rel="icon" type="image/png" href="favicons/favicon-16x16.png" sizes="16x16">
    <link rel="manifest" href="favicons/manifest.json">
    <link rel="shortcut icon" href="favicons/favicon.ico">
    
        <!-- JavaScript Imports -->
    <script type="text/javascript" src="js/jquery.min.js"></script>
    <script type="text/javascript" src="js/bootstrap.min.js"></script>
    <script type="text/javascript" src="js/scripts.js"></script>
</head>
	<body>
	""")



def html_body_top():
    print("""
    <div class="container">
	<div class="row clearfix">
		<div class="col-md-12 column text-center">
			<h2 class="title ">Pillow<span class="highlight">Pi</span></h2>
			<p>
				Welcome to the PillowPi Web Interface. Visit <a href="sedders123.github.io/PillowPi" target="_blank">our website</a> for full documentation 
			</p>
            <div class="row clearfix">""")
    
def html_body_main(light,temp):
    if light == "HIGH":
        print("""
        <div class="col-md-6 column">
                    <h2>Light Levels</h2>
                    <div>
                        <div class="circle-red"><div class="title">Too Bright</div></div>
                    </div>
                        
				</div>
        """)
    elif light == "OK":
        print("""
        <div class="col-md-6 column">
                    <h2>Light Levels</h2>
                    <div>
                        <div class="circle-green"><div class="title">OK</div></div>
                    </div>
                        
				</div>
        """)
    else:
        print("""
        <div class="col-md-6 column">
                    <h2>Light Levels</h2>
                    <div>
                        <div class="circle-amber"><div class="title">ERROR</div></div>
                    </div>
                        
				</div>
        """)
    if temp == "HIGH":
        print("""
        <div class="col-md-6 column">
                    <h2>Temeprature</h2>
                    <div>
                        <div class="circle-red"><div class="title">Too Hot</div></div>
                    </div>
				</div>
        """)
    elif temp == "OK":
        print("""
        <div class="col-md-6 column">
                    <h2>Temeprature</h2>
                    <div>
                        <div class="circle-green"><div class="title">OK</div></div>
                    </div>
				</div>
        """)
    else:
        print("""
        <div class="col-md-6 column">
                    <h2>Temeprature</h2>
                    <div>
                        <div class="circle-amber"><div class="title">ERROR</div></div>
                    </div>
				</div>
        """)
        
def html_body_bottom():
    print("""
    			</div>
		</div>
	</div>
</div>
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
        Running = True
        while Running:
            main()
            html_body_top()
            html_body_main(light, temp)
            html_body_bottom()
            sleep(5)
	
	
