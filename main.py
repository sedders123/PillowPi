import RPi.GPIO as GPIO
from time import sleep
import pygame.mixer
import pygame.mixer_music

GPIO.setmode(GPIO.BCM)

GPIO.setup(23, GPIO.IN) # Light
GPIO.setup(24, GPIO.IN) # Temp
GPIO.setup(6, GPIO.IN) # Butt_0
GPIO.setup(5, GPIO.IN) # Butt_1
GPIO.setup(26, GPIO.OUT) # Green
GPIO.setup(19, GPIO.OUT) # Amber
GPIO.setup(13, GPIO.OUT) # Red

ambient = "Forest.mp3"
red = "Red.mp3"
amber = "Amber.mp3"
green = "Green.mp3"

Running = True

def sound_init():
    pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)
    pygame.mixer_music.set_volume(10)

def sound_play(state):
    if state == "Green":
        pygame.mixer_music.load("Green.mp3")
    elif state == "Amber":
        pygame.mixer_music.load("Amber.mp3")
    else:
        pygame.mixer_music.load("Red.mp3")
    pygame.mixer_music.play()

while Running == True:
    sound_init()
    
    if GPIO.input(23) == True:
        print("Light: HIGH")
    else:
        print("Light: OK")

    if GPIO.input(24) == True:
        print("Temperature: HIGH")
    else:
        print("Temperature: OK")

    if GPIO.input(23) == False and GPIO.input(24) == False:
        state = "Green"
        print("Green")
        GPIO.output(26, True)
        

    elif (GPIO.input(23) == False and GPIO.input(24) == True) or (GPIO.input(23) == True and GPIO.input(24) == False):
        state = "Amber"
        print("Amber")
        GPIO.output(19, True)

    else:
        print("Red")
        GPIO.output(13, True)

    if GPIO.input(6) == True:
        print("Button 1 pressed")
        sound_play(state)

    if GPIO.input(5) == True:
        print("Button 2 pressed")
        pygame.mixer.quit()
        sound_init()
        pygame.mixer_music.load("Forest.mp3")
        pygame.mixer_music.play()
        pygame.mixer_music.fadeout(20)
        
    sleep(1)

    GPIO.output(26, False)
    GPIO.output(19, False)
    GPIO.output(13, False)
    pygame.mixer.quit()
