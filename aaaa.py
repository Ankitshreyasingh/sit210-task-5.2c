from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO
RPi.GPIO.setmode(RPi.GPIO.BCM)

## Hardware
ledRed = LED(14)
ledGreen = LED(15)
ledBlue = LED(16)

## Gui Definitions
win=Tk()
win.title("SIT210 - 5.2C")
win.geometry("200x90")
myFont = tkinter.font.Font(family = 'Helvetica', size = 12, weight = 'bold')

## Event functions
def ledAllOff():
    ledRed.off()
    ledGreen.off()
    ledBlue.off()

def ledToggle():
    ledOption = str(value.get())
    label.config(text = ledOption)
    ledAllOff()

    if ledOption == 'red':
        ledRed.on()
    if ledOption == 'green':
        ledGreen.on()
    if ledOption == 'blue':
        ledBlue.on()

def close():
    RPi.GPIO.cleanup()
    win.destroy()

## widgets
value  =  StringVar ()
redButton  =  Radiobutton ( win,  text = "Red" ,  variable = value ,  value = 'red' ,
    command = ledToggle)
greenButton  =  Radiobutton ( win ,  text = "Green" ,  variable = value ,  value = 'green' ,
    command = ledToggle)
blueButton  =  Radiobutton ( win ,  text = "Blue",  variable = value ,  value = 'blue' ,
    command = ledToggle)
redButton.pack(anchor = W)
greenButton.pack(anchor = W)
blueButton.pack(anchor = W)

label = Label(win)
label.pack()

win.protocol("WM_DELETE_WINDOW", close) # Close cleanly when clicking window X..

win.mainloop() # Loop forever and keep GUI running.





from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO
RPi.GPIO.setmode (RPi.GPIO.BCM)

## Hardware
redLED = 11
blueLED = 13
greenLED = 15

GPIO.setup(redLED, GPIO.OUT)
GPIO.output(redLED, GPIO.LOW)
GPIO.setup(blueLED, GPIO.OUT)
GPIO.output(redLED, GPIO.LOW)
GPIO.setup(greenLED, GPIO.OUT)
GPIO.output(greenLED, GPIO.LOW)

#GUI Definitions
win = Tk()
value = IntVar()
win.title("LED Toggle")
myFont = tkinter.font.Font(family="Helvetica", size=12, weight="bold")

## Events function
def rLEDToggle():
    if GPIO.input(11)==1:
        GPIO.output(redLED, GPIO.HIGH)
        red_button["test"] = "Turn on red LED"

    else:
        GPIO.output(redLED, GPIO.LOW)
        red_button["text"] = "Turn off red LED"

def bLEDToggle():
    if GPIO.input(13)==1:
        GPIO.output(blueLED, GPIO.HIGH)
        yellow_button["test"] = "Turn on blue LED"

    else:
        GPIO.output(blueLED, GPIO.LOW)
        yellow_button["text"] = "Turn off blue LED"

def gLEDToggle():
    if GPIO.input(15)==1:
        GPIO.output(greenLED, GPIO.LOW)
        green_button["text"] = "Turn on green LED"

    else:
        GPIO.output(greenLED, GPIO.HIGH)
        green_button["text"] = "Turn off green LED"

def close():
    RPi.GPIO.cleanup()
    win.destroy()


## Widgets

red_button = Radiobutton( win, text = "RED LED", font = myFont, variable = value, value = 1, command = rLEDToggle, bg = 'bisque2', height = 1, width = 8)
red_button.grid( row = 1, column = 0)

yellow_button = Radiobutton( win, text = "YELLOW LED", font = myFont, variable = value, value= 2, command = bLEDToggle, bg = 'bisque2', height = 1, width = 8)
yellow_button.grid( row = 1, column = 1)

green_button = Radiobutton( win, text = "GREEN LED", font = myFont, variable = value, value = 3, command = gLEDToggle, bg = 'bisque2', height = 1, width = 8)
green_button.grid( row = 1, column = 2)

close_button = Radiobutton( win, text = "EXIT", font = myFont,command = close, height = 1, width = 5)
close_button.grid( row = 2, column = 3)

win.mainloop()
