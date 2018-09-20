'''
Created on Oct 10, 2017

@author: deepak
'''
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector as mysql
import GUIdb as guiconf
from pip._vendor.colorama.ansi import Style
from DataBase.DataConnection import GUIDB
conn = mysql.connect(**guiconf.dbconf)


class MyClass(object):
    '''
    classdocs
    '''
    

    def __init__(self, master):
        '''
        Constructor
        
        '''
        master.title('Voter Search Software Application')
        master.resizable(False, False)
        master.configure(background = '#bdbdbd')
        
        self.style = ttk.Style()
        self.style.configure('TFrame', background = '#2979ff')
        self.style.configure('TButton', background = '#2979ff',font = ('Arial', 14))
        self.style.configure('TLabel', background = '#2979ff', font = ('Arial', 14))
        self.style.configure('Header.TLabel', font = ('Arial', 18, 'bold'))
        
        
        #self.master.geometry('640x480+200+200')
        self.headFram = ttk.Frame(master)
        self.headFram.pack()
        
        self.logo = PhotoImage(file = 'C:\\Users\\deepa\\Downloads\\Video\\Lynda_Python_GUI\\Ex_Files_Python_Tkinter\\Exercise Files\\Ch08\\tour_logo.gif')
        ttk.Label(self.headFram,image = self.logo).grid(row=0, column = 0,rowspan = 2,padx = 25)
        ttk.Label(self.headFram,text = "Voter List Search", style = 'Header.TLabel').grid(row= 0,column = 1,padx = 20)
        ttk.Label(self.headFram,text = "Developed By :- Deepak,Harshada and komal").grid(row=1, column = 1,padx = 20)
        
        
        #=================Display Frame=====================
        self.displayFram = ttk.Frame(master)
        self.displayFram.pack()
        
        self.text_comments = Text(self.displayFram, width = 130, height =20)
        
        
        ttk.Label(self.displayFram,text = 'Voter No').grid(row=0, column = 0,pady = 10,padx = 10)
        ttk.Label(self.displayFram,text = 'LastName').grid(row=0, column = 1,pady = 10,padx = 10)
        ttk.Label(self.displayFram,text = 'FirstName').grid(row=0, column = 2,pady = 10,padx = 10)
        ttk.Label(self.displayFram,text = 'MiddleName').grid(row=0, column = 3,pady = 10,padx = 10)
        ttk.Label(self.displayFram,text = 'Address').grid(row=0, column = 4,pady = 10,padx = 10)
        ttk.Label(self.displayFram,text = 'FamilyID').grid(row=0, column = 5,pady = 10,padx = 10)
        
        self.text_comments.grid(row = 1,column = 0,padx = 10,columnspan = 6)
        # code for display
        
        #self.text_comments.insert('1.0 + 2 lines', 'Inserted message')
       
        
        #=================Search Frame============================ 
        self.searchFram = ttk.Frame(master)
        self.searchFram.pack()
        
        ttk.Label(self.searchFram,text = 'LastName').grid(row=0, column = 0,pady = 10)
        ttk.Label(self.searchFram,text = 'FirstName').grid(row=0, column = 1,pady = 10)
        ttk.Label(self.searchFram,text = 'MiddleName').grid(row=0, column = 2,pady = 10)
        
        self.entry_lastname = ttk.Entry(self.searchFram, width = 30)
        self.entry_Firstname = ttk.Entry(self.searchFram, width = 30)
        self.entry_middlename = ttk.Entry(self.searchFram, width = 30)
        
        self.entry_lastname.grid(row=1, column = 0, padx = 10,pady = 5)
        self.entry_Firstname.grid(row=1, column = 1, padx = 10,pady = 5)
        self.entry_middlename.grid(row=1, column = 2, padx = 10,pady = 5)
        
        ttk.Button(self.searchFram,text = 'Search',command = self.search).grid(row=2, column = 0,columnspan = 2,pady = 10)
        ttk.Button(self.searchFram,text = 'Clear',command = self.clear).grid(row=2, column = 1,columnspan = 2,pady = 10)
        
        #self.okFrame = ttk.Button(self.searchFram,text = 'OK',command = self.topwindow).grid(row=3, column = 1,pady = 10)
        ttk.Button(self.searchFram,text = 'OK',command = self.topwindow).grid(row=3, column = 1,pady = 10)
        
        #self.okFrame.state(['disabled'])
        
    def search(self):
        
        
        #lName = StringVar()
        #lsearch = StringVar()
        lName = self.entry_lastname.get()
        fName = self.entry_Firstname.get()
        mName = self.entry_middlename.get()
        #print(lName)
        try:
            
            GUIDB= "voter"
            cursor = conn.cursor()
            #print(cursor.execute("SHOW DATABASES"))
            cursor.execute("USE VOTER")
            
            a = "SELECT voterno,lastname,firstname,middlename,polladd,familyid FROM YADI WHERE (lastname = '{}') OR (firstname = '{}') OR (middlename = '{}')".format(lName,fName,mName) 
            
            #lsearch =  cursor.execute("SELECT * FROM LIST WHERE (lastname = '{}') OR (firstname = '{}') OR (middlename = '{}')".format(lName,fName,mName))
            if cursor.execute(a) is not True:
                
            #self.text_comments.insert('1.0 + 2 lines', '{}'.format(lsearch))
            
                results = cursor.fetchall()
                
                for row in results:
                    
                    voterno = row[0]
                    lastname = row[1]
                    firstname = row[2]
                    middlename = row[3]
                    polladd = row[4]
                    familyid = row[5]
                    
                    #print(voterno,lastname,firstname,middlename,polladd,familyid)
                    self.text_comments.insert('1.0 + 2 lines','{} \t'.format(voterno))
                    self.text_comments.insert('1.0 + 2 lines','{} \t'.format(lastname))
                    self.text_comments.insert('1.0 + 2 lines','{} \t'.format(firstname))
                    self.text_comments.insert('1.0 + 2 lines','{} \t'.format(middlename))
                    self.text_comments.insert('1.0 + 2 lines','{} \t'.format(polladd))
                    self.text_comments.insert('1.0 + 2 lines','{} \t'.format(familyid))
                    self.text_comments.insert('1.0 + 2 lines','\n')
                    
                    #self.okFrame.instate(['disabled'])
                
                # commite our query..
                conn.commit()
            else:
                messagebox.showinfo(title = "Notification", message = 'Name Not Found')
                
        except:
            conn.rollback()

        
        
    
    def clear(self):
        self.entry_lastname.delete(0, 'end')
        self.entry_Firstname.delete(0, 'end')
        self.entry_middlename.delete(0, 'end')
        self.text_comments.delete(1.0, 'end')  
       
       #====================Top Window Clicked By Ok Button
    def topwindow(self):
        
        lName = self.entry_lastname.get()
        fName = self.entry_Firstname.get()
        mName = self.entry_middlename.get()
        
        window = Toplevel(self.headFram)
        window.geometry('950x520+200+30')
        window.title('Voter Information')
        
        panedwindow = ttk.Panedwindow(window, orient = HORIZONTAL)
        panedwindow.pack(fill = BOTH, expand = True)
        
        infoFram = ttk.Frame(panedwindow, width = 200, height = 300, relief = SUNKEN)
        familyFram = ttk.Frame(panedwindow, width = 200, height = 300, relief = SUNKEN)
        
        panedwindow.add(infoFram, weight = 4)
        panedwindow.add(familyFram, weight = 1)
        
        ttk.Label(infoFram,text = 'LastName:-').grid(row=0, column = 0,pady = 10,padx = 10)
        ttk.Label(infoFram,text = 'FirstName:-').grid(row=1, column = 0,pady = 10,padx = 10)
        ttk.Label(infoFram,text = 'MiddleName:-').grid(row=2, column = 0,pady = 10,padx = 10)
        
        entrylastname = ttk.Entry(infoFram, width = 30)
        entryFirstname = ttk.Entry(infoFram, width = 30)
        entrymiddlename = ttk.Entry(infoFram, width = 30)
        
        entrylastname.grid(row = 0, column =1,padx = 20)
        entryFirstname.grid(row = 1, column =1,padx = 20)
        entrymiddlename.grid(row = 2, column =1,padx = 20)
        
        ttk.Label(infoFram,text = 'Polling Address:-').grid(row=3, column = 0,pady = 10,padx = 10)
        ttk.Label(infoFram,text = 'Card No:-').grid(row=4, column = 0,pady = 10,padx = 10)
        ttk.Label(infoFram,text = 'Family Id:-').grid(row=5, column = 0,pady = 10,padx = 10)
        ttk.Label(infoFram,text = 'Contact No:-').grid(row=6, column = 0,pady = 10,padx = 10)
        
        entryPoll = ttk.Entry(infoFram, width = 50)
        entryCard = ttk.Entry(infoFram, width = 20)
        entryFamily = ttk.Entry(infoFram, width = 20)
        entryContact = ttk.Entry(infoFram, width = 20)
        
        entryPoll.grid(row = 3, column =1,padx = 20)
        entryCard.grid(row=4, column = 1,padx = 20)
        entryFamily.grid(row =5,column = 1,padx = 20)
        entryContact.grid(row = 6,column = 1,padx = 20)
        cursor = conn.cursor()
        
        b = "SELECT * FROM YADI WHERE (lastname = '{}') OR (firstname = '{}') OR (middlename = '{}')".format(lName,fName,mName)
        
        results = cursor.fetchall()
                
        for row in results:
                    
            voterno = row[0]
            lastname = row[1]
            firstname = row[2]
            middlename = row[3]
            polladd = row[4]
            familyid = row[5]
            cardno = row[6]
            familyid = row[7]
            
                    
        

def main():
   root = Tk()
   root.geometry('1080x720+200+30')
   
   app = MyClass(root)
   root.mainloop()
   conn.close()
   
   
if __name__ == '__main__':main()   