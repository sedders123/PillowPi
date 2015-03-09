#!C:\Python32\python.exe
#the above line specifies the path where the Python Interpreter is installed on the web server

import cgi

def http_header():
        '''generates http header'''
        print("Content-type:text/html\n")

##The script MUST output the HTTP header.
##The HTTP header consists of one or more messages followed by a blank line
##If the script is to be interpreted as HTML then the content type will be text/html.
##\n (following text/html) generates the required blank line	

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

if __name__=="__main__":
        http_header()
        html_top()
        print("Hello World")
        html_bottom()
	
	
