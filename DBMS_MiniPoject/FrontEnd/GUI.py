from tkinter import *
from tkinter import ttk

class Frontend:
    
    def __init__(self, master):

        #self.label = ttk.Label(master, text = "Hello, Tkinter!")
        #self.label.grid(row = 0, column = 0, columnspan = 2)
        self.firstName = ttk.Label(master,text = "First Name")
        self.firstName.place(x=150,y=350)
        #self.firstName.grid(row = 5,column = 5)
        
        self.firstName.config(foreground = 'blue',font = ('Courier', 18, 'bold'))
   





def main():
    root = Tk()
    root.geometry('950x650+350+100')
    root.title("Voter Search" )
    
    app= Frontend(root)
   # app.label_display(root)
    root.mainloop()
    
    
    
if __name__ == '__main__':
    main()
    