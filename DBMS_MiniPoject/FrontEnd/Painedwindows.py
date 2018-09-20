'''
Created on Oct 9, 2017

@author: deepak
'''
from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Voter')

panedwindows = ttk.Panedwindow(root,orient = VERTICAL)
panedwindows.pack(fill = BOTH, expand  = True)

frame1 = ttk.Frame(panedwindows,width = 100, height = 300, relief = SUNKEN)
frame2 = ttk.Frame(panedwindows,width = 400, height = 400, relief = SUNKEN)
panedwindows.add(frame1,weight = 1)
panedwindows.add(frame2,weight = 4)

frame3 = ttk.Frame(panedwindows,width = 50, height = 400, relief = SUNKEN)
panedwindows.insert(1, frame3)



root.mainloop()