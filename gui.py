# -*- coding: utf-8 -*-
"""
Created on Mon Dec 27 00:05:59 2021

@author: Apurva
"""

import os
from tkinter import *

def save_info():
   firstname_info = firstname.get()
   save_info.fname = firstname_info
   label.config( text = clicked.get() )
   save_info.text = clicked.get()
   screen.destroy()
     

screen = Tk()
screen.geometry("500x500")
screen.title("Smart Attendence System")
heading = Label(text = "Smart Attendence System", bg="grey", fg="black", width="500", height="3")
heading.pack()

firstname_text = Label(text="Enter Subject Name")
firstname_text.place(x=15,y=70)

firstname = StringVar()

firstname_entry = Entry(textvariable = firstname, width ="30")

firstname_entry.place(x=15,y=100)

options = [
	"3rd Year",
	"4th Year"
	
]

clicked = StringVar()

# initial menu text
clicked.set( "4th Year" )

label = Label( screen , text = " Enter Year" )
label.place(x=15,y=150)

# Create Dropdown menu
drop = OptionMenu( screen , clicked , *options )
drop.place(x=15,y=170)

# Create button, it will change label text


# Create Label



register = Button(screen,text = "Start", width="10",height="2", command=save_info)
register.place(x=15,y=250)





screen.mainloop()