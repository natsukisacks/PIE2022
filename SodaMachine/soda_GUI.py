from tkinter import *
import tkinter.font as font
import serial
import time

# Open serial if not open
# NOTE: Arduino must be plugged in but needs to have the Serial Monitor closed
ser = serial.Serial(port='COM11', baudrate=9600, timeout=0)
if not ser.isOpen():
    ser.open()
print('COM7 is open: ', ser.isOpen())

# If we decide we want to full screen: https://pythonguides.com/python-tkinter-window-size/
win = Tk() # Create the window
intVar = IntVar() # Why do we need things like this?
win.title("Soda Machine")
win.geometry('800x600+250+100') # WIDTHxHEIGHT+X_POS+Y_POS
win['background'] = '#add8e6' # light blue

valves = [] 
amountList = []

def btnCallback(drinkName, textbox):
    # Callback for choosing a drink. Adds that drink to the textbox
    # to help the user keep track
    textbox.insert('end', drinkName + '\n')

def cCallback(valve, amount):
    # Callback for checking checkbox. Appends information to arrays.
    valves.append(str(valve))
    amountList.append(str(amount))

def sendSerial(valve, amounts):
    # Merge lists to send ["amount", "valve", "amount", etc..] through serial
    merge = []
    for i in range(len(valve)):
        merge.append(amounts[i])
        merge.append(valve[i])
    serialStr = ",".join(merge)
    print("Sent:", serialStr)
    ser.write(str.encode(serialStr))

# Labels
generalFont = font.Font(family='Courier New', size=16)
buttonFont = font.Font(family='Courier New', size=12)
smallFont = font.Font(family='Courier New', size=8)
greeting = Label(win, text="What would you like to drink?", fg='#00008b', font=generalFont)
prompt = Label(win, text="Choose your drinks and amounts (mL):", fg='#00008b', font=generalFont)
clearInfo = Label(win, text="Press RESTART to clear", fg='#00008b', font=smallFont)

# Amount choices
amtOptions = ["0", "10", "30", "50", "100"]
stringVar1 = StringVar(win)
stringVar1.set(amtOptions[0]) # set default value
stringVar2 = StringVar(win)
stringVar2.set(amtOptions[0])
stringVar3 = StringVar(win)
stringVar3.set(amtOptions[0])
stringVar4 = StringVar(win)
stringVar4.set(amtOptions[0])

# Create option dropdown menus
amtMenuCoke = OptionMenu(win, stringVar1, *amtOptions)
amtMenuSprite = OptionMenu(win, stringVar2, *amtOptions)
amtMenuIcedTea = OptionMenu(win, stringVar3, *amtOptions)
amtMenuLemonade = OptionMenu(win, stringVar4, *amtOptions)

# Create check buttons
filler = ""
cSprite = Checkbutton(win, text='Done?', variable=filler, onvalue=1, offvalue=0, command=lambda: cCallback(1, stringVar1.get()))
cCoke = Checkbutton(win, text='Done?', variable=filler, onvalue=1, offvalue=0, command=lambda: cCallback(2, stringVar2.get()))
cIcedTea = Checkbutton(win, text='Done?', variable=filler, onvalue=1, offvalue=0, command=lambda: cCallback(3, stringVar3.get()))
cLemonade = Checkbutton(win, text='Done?', variable=filler, onvalue=1, offvalue=0, command=lambda: cCallback(4, stringVar4.get()))

# Create drink buttons
selectionUpdate = Text(win, height=12, width=40)
coke = Button(win, text = 'MOUNTAIN DEW', font = buttonFont, bd = '5', bg = '#d2b48c', command=lambda: btnCallback("mountain dew", selectionUpdate))
sprite = Button(win, text = 'BAJA BLAST', font = buttonFont, bd = '5', bg = '#d2b48c', command=lambda: btnCallback("baja blast", selectionUpdate))
icedTea = Button(win, text = 'GRAPE GATORADE', font = buttonFont, bd = '5', bg = '#d2b48c', command=lambda: btnCallback("grape gatorade", selectionUpdate))
lemonade = Button(win, text = 'PINK LEMONADE', font = buttonFont, bd = '5', bg = '#d2b48c', command=lambda: btnCallback("pink lemonade", selectionUpdate))
serialButton = Button(win, text = 'MAKE MY DRINK!', font = generalFont, bd = '2', bg = '#8ABD91', command=lambda: sendSerial(valves, amountList)) # calls lambda which calls other function
kill = Button(win, text = 'RESTART', font = generalFont, bd = '2', bg = '#FF7276', command=lambda: win.quit())

# Place text
selectionUpdate.place(x=250, y=60)
selectionUpdate.insert('end', "YOU HAVE SELECTED:\n")
greeting.place(x=230, y=10)
prompt.place(x=190, y=280)
clearInfo.place(x=635, y=520)

# Place buttons
kill.place(x=680, y=550) # bottom right
serialButton.place(x=325, y=550) # bottom middle
coke.place(x=100, y=330)
sprite.place(x=250, y=330)
icedTea.place(x=380, y=330)
lemonade.place(x=550, y=330)

# Place dropdown menus
amtMenuCoke.place(x=150, y=390)
amtMenuSprite.place(x=290, y=390)
amtMenuIcedTea.place(x=430, y=390)
amtMenuLemonade.place(x=590, y=390)

# Place final checkboxes
cSprite.place(x=145, y=440)
cCoke.place(x=285, y=440)
cIcedTea.place(x=425, y=440)
cLemonade.place(x=585, y=440)

win.mainloop()
