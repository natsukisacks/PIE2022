from tkinter import *
import tkinter.font
import RPi.GPIO as GPIO

win = Tk()
win.title("Test")


myFont = tkinter.font.Font(family = 'Helvetica', size = 36, weight = 'bold')
button = Button(win, text = "Tester", font = myFont, bg = 'bisque2', height = 1, width = 4)
