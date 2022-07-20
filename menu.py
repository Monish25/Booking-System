import tkinter as tk
import os
from tkinter import messagebox
import welcome

def login():
    def run():
        rootA.destroy()
        r.destroy()
        menu()
    
    creds = 'Logg.WDC' 
    def Login():
        global nameEL
        global pwordEL 
        global rootA
     
        rootA = tk.Tk() 
        rootA.title('Login') 
        rootA.geometry('250x150')
     
        intruction = tk.Label(rootA, text='Enter User Name \n & password\n') 
        intruction.grid(row = 0, column = 1) 
     
        nameL = tk.Label(rootA, text='Username: ') 
        pwordL = tk.Label(rootA, text='Password: ') 
        nameL.grid(row=1)
        pwordL.grid(row=2)
     
        nameEL = tk.Entry(rootA) 
        pwordEL = tk.Entry(rootA, show='*')
        nameEL.grid(row=1, column=1)
        pwordEL.grid(row=2, column=1)
     
        loginB = tk.Button(rootA, text='Login', command=CheckLogin) 
        loginB.grid(row = 3,column = 1)
    
        rootA.mainloop()
     
    def CheckLogin():
        global r
        with open(creds) as f:
            data = f.readlines() 
            uname = data[0].rstrip() 
            pword = data[1].rstrip() 
     
        if nameEL.get() == uname and pwordEL.get() == pword: 
            r = tk.Tk() 
            r.title('Login Success')
            r.geometry('250x70') 
            rlbl = tk.Label(r, text='\n Successfully Logged In') 
            rlbl.pack() 
            launch = tk.Button(r,text = 'Start',command = run)
            launch.pack()
            r.mainloop()
        else:
            r = tk.Tk()
            r.title('INVALID')
            r.geometry('150x70')
            rlbl = tk.Label(r, text='\n Invalid Login')
            rlbl.pack()
            rbutx = tk.Button(r,text = 'Retry',command = r.destroy)
            rbutx.pack()
            r.mainloop()
     
     
    if os.path.isfile(creds):
        Login()
    


def BUS():
    a.destroy()
    os.system('viewbus.py')
def TRAIN():
    a.destroy()
    os.system('viewrail.py')    
def FLIGHT():
    a.destroy()
    os.system('viewflight.py')    
def BUSb():
    a.destroy()
    os.system('viewbus.py')
def TRAINb():
    a.destroy()
    os.system('viewrail.py')    
def FLIGHTb():
    a.destroy()
    os.system('viewflight.py')   
def BUSi():
    a.destroy()
    os.system('insbus.py')
def TRAINi():
    a.destroy()
    os.system('instrain.py')    
def FLIGHTi():
    a.destroy()
    os.system('insflight.py')   


def book():
    global a
    a=tk.Tk()
    a.geometry('250x200')
    l = tk.Label(a,text = 'CHoice',bg = "grey",width = '43', height = "1", font = ("Lucida Handwriting", 13))
    c1=tk.Button(a,text='Bus',width=12,height=1,command=BUSb,padx=5, pady=10)
    c2=tk.Button(a,text='Train',width=12,height=1,command=TRAINb,padx=5, pady=10)
    c3=tk.Button(a,text='Flight',width=12,height=1,command=FLIGHTb,padx=5, pady=10)
    l.pack()
    c1.pack()
    c2.pack()
    c3.pack()
    a.mainloop()

def insert():
    global a
    a=tk.Tk()
    a.geometry('250x200')
    l = tk.Label(a,text = 'CHoice',bg = "grey",width = '43', height = "1", font = ("Lucida Handwriting", 13))
    c1=tk.Button(a,text='Bus',width=12,height=1,command=BUSi,padx=5, pady=10)
    c2=tk.Button(a,text='Train',width=12,height=1,command=TRAINi,padx=5, pady=10)
    c3=tk.Button(a,text='Flight',width=12,height=1,command=FLIGHTi,padx=5, pady=10)
    l.pack()
    c1.pack()
    c2.pack()
    c3.pack()
    a.mainloop()



def viewrecords():
    global a
    a=tk.Tk()
    a.geometry('250x200')
    l = tk.Label(a,text = 'CHoice',bg = "grey",width = '43', height = "1", font = ("Lucida Handwriting", 13))
    c1=tk.Button(a,text='Bus',width=12,height=1,command=BUS,padx=5, pady=10)
    c2=tk.Button(a,text='Train',width=12,height=1,command=TRAIN,padx=5, pady=10)
    c3=tk.Button(a,text='Flight',width=12,height=1,command=FLIGHT,padx=5, pady=10)
    l.pack()
    c1.pack()
    c2.pack()
    c3.pack()
    a.mainloop()


def credit():
    C1 = tk.Tk()
    C1.geometry('400x100')
    L1 = tk.Label(C1,text = 'Ticket booking Service\n Made By Ashwin,Monish,Saran\n Using Python 3.7.0 and MySQL 5.7')
    B1 = tk.Button(C1,text = 'Exit',width = 2, height = 1,command = C1.destroy)
    L1.pack()
    B1.pack()
    C1.mainloop()
def menu():
    D1 = tk.Tk()
    D1.geometry('500x350')
    D1.title('Menu')
    L1 = tk.Label(D1,text = 'TICKET BOOKING',bg = "grey",width = '43', height = "1", font = ("Lucida Handwriting", 13))
    B1 = tk.Button(D1, text = 'Booking',width = 12,height = 1,command = book)
    B2 = tk.Button(D1, text = 'View Records',width = 12,height = 1,command = viewrecords)
    B3 = tk.Button(D1, text = 'Insert Records',width = 12,height = 1,command = insert)
    B4 = tk.Button(D1, text = 'Credits',width = 12,height = 1,command = credit)
    B5 = tk.Button(D1, text = 'Exit',command = D1.destroy,width = 12,height = 1)
    
    L1.grid(column = 0,row = 0,columnspan=6)
    B1.grid(column = 1,row = 1,padx=5, pady=10)
    B2.grid(column = 1,row = 2,padx=5, pady=10)
    B3.grid(column = 3,row = 1,padx=5, pady=10)
    B4.grid(column = 3,row = 2,padx=5, pady=10)
    B5.grid(column = 2,row = 3,padx=5, pady=10)
    
    D1.mainloop()
if os.path.isfile('Logg.WDC'):
    if os.path.isfile('db.WDC'):
        welcome.run()
        login()
    else:
        r = tk.Tk()
        r.geometry('500x50')
        r.title('Erx01')
        l = tk.Label(r,text = 'ERx01 : Some Files are Missing,Contact Admin')
        l.pack()
        b = tk.Button(r,text = 'Ok',command = r.destroy)
        b.pack()
        r.mainloop()
        
    
else:
    r = tk.Tk()
    r.geometry('500x50')
    r.title('Erx01')
    l = tk.Label(r,text = 'ERx01 : Some Files are Missing,Contact Admin')
    l.pack()
    b = tk.Button(r,text = 'Ok',command = r.destroy)
    b.pack()
    r.mainloop()