import os
from tkinter import * # GUI Framework
from tkinter import ttk # GUI Framework

disableSleep = 0

root = Tk()
root.title("pmset")
root.geometry("200x100")

def disableSleep():
    os.system("sudo pmset -a disablesleep 1")
    quitButton.config(bg="red", fg="red")

def enableSleep():
    os.system("sudo pmset -a disablesleep 0")
    quitButton.config(bg="green", fg="green")

disableSleepButton = Button(root, text="Disable sleep", command=disableSleep)
disableSleepButton.grid(row=0, column=0)

enableSleepButton = Button(root, text="Enable sleep", command=enableSleep)
enableSleepButton.grid(row=1, column=0)

quitButton = Button(root, text= "Quit", command=root.destroy)
quitButton.grid(row=2, column=0)



root.mainloop()
