'''
Created on Oct 8, 2017

@author: deepak
Topic : Frame child frame
'''
from tkinter import *
from tkinter import ttk

#===========Parent Frame===============
root = Tk()

#==========Create Child Fram============
fram = ttk.Frame(root)
fram.pack()
fram.config(height = 100,width = 200)
fram.config(relief = RIDGE)

#==========Puting Button into fram=========
ttk.Button(fram,text='Search').grid()
fram.config(padding = (30,15))

#============Label Fram==============
ttk.Labelframe(root,height = 100,width = 200,text = 'My frame').pack()


root.mainloop()