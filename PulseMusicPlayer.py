import random
import sys
import os
import vlc
import tkinter
from tkinter import *
from tkinter import messagebox as tkMessageBox
from tkinter import filedialog
import easygui
from PIL import Image



window = tkinter.Tk()
window.geometry('500x500')
window.wm_title('Pulse Music Player')



## Menu Functions
def donothing():
	filewin = TopLevel(window)
	button = Button(filewin, text = "Do Nothing Button")
	button.pack

## Menu Structure for the Music Player

song = filedialog.askopenfilename()

menubar = Menu(window)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=donothing)
filemenu.add_command(label="Open", command= donothing)
filemenu.add_command(label="Save", command=donothing)
filemenu.add_command(label="Save as...", command=donothing)
filemenu.add_command(label="Close", command=donothing)


filemenu.add_command(label="Exit", command=window.quit)
menubar.add_cascade(label="File", menu=filemenu)

helpmenu = Menu(menubar, tearoff=0)

helpmenu.add_command(label="About...", command=donothing)



## Buttons for Playing a stoping the song

def PlayButton():
	global g
	g = vlc.MediaPlayer(song)
	g.play()

def pause():
	g.pause()
		
def stop():
	g.stop()
	
Play = tkinter.Button(window, text = "Play" , command = PlayButton, )

Pause = tkinter.Button(window, text = "Pause or Continue", command = pause)

Stop = tkinter.Button(window, text = "Stop", command = stop)


#ButtonData

Canvas = tkinter.Canvas(window, height=450 , width=350)

img = PhotoImage(file="Empire-pilot.gif")




Canvas.pack()
Play.pack()
Play.place(relx =0 , rely = .9,)
Pause.pack()
Stop.pack()
Stop.place(relx =.500, rely = 0)
window.config(menu=menubar)
Canvas.create_image(100,100, anchor=NW, image=img)
window.mainloop()
