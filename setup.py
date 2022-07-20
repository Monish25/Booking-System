import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk,Image
import os
import mysql.connector
import welcome
File = 'Logg.WDC'
dbcrd = 'db.WDC'
def sqlsetup():
    os.system('sqlsetup.py')
def ins():
    global setN
    setN = tk.Tk()
    setN.title('Your Name')
    setN.geometry('450x250')
    heading = tk.Label(text = "SETUP :)", bg = "grey",width = '43', height = "1", font = ("Lucida Handwriting", 13))
    L1 = tk.Label(setN, text='Welcome to the setup of the program, \nMake sure u have the correct SQL information and\n All the minimum requirements resolved for the smooth working of the setup:\n\nMINIMUM REQUIREMENTS\n1.Requires mySQL 5.7\n2.Python Docx Module\n\n When Verifing SQL Connection\n A small window will come, If not It means it is not verified')
    
    B1 = tk.Button(setN, text = 'Next',command = sql)
   
    heading.grid(row=0, column=0,columnspan = 12)
    
    
    L1.grid(row =1 , column =1,padx = 10, pady=10)
    B1.grid(row =2 , column =1,padx = 10, pady=10)
    setN.mainloop()
    sql()

def sql():
    setN.destroy()
    global E1
    global E2
    global E3
    global setSQL
    setSQL = tk.Tk()
    setSQL.title('SQL Login')
    setSQL.geometry('450x250')
    heading = tk.Label(text = "SQL", bg = "grey",width = '43', height = "1", font = ("Lucida Handwriting", 13))

    L1 = tk.Label(setSQL, text='Enter Your User Name:')
    L2 = tk.Label(setSQL, text = 'Enter your Password:')
    L3 = tk.Label(setSQL, text='Enter Your Local Host:')
    B1 = tk.Button(setSQL, text = 'Verify',command = verify)
    B2 = tk.Button(setSQL, text = 'Next',command = login)
    E1 = tk.Entry(setSQL)
    E2 = tk.Entry(setSQL,show = '*')
    E3 = tk.Entry(setSQL)
    
    heading.grid(row=0, column=0, columnspan=8)
    E1.grid(row =1 , column =2,padx = 10, pady=10 )
    E2.grid(row =2 , column =2,padx = 10, pady=10 )
    E3.grid(row =3, column = 2,padx = 10, pady=10)
    L1.grid(row =1, column =1 ,padx = 10, pady=10)
    L2.grid(row =2 , column =1,padx = 10, pady=10 )
    L3.grid(row =3 , column =1,padx = 10, pady=10 )
    B1.grid(row =4 ,column = 2,padx = 10, pady=10)
    B2.grid(row =5 ,column = 2,padx = 10, pady=10)
    setSQL.mainloop()
    
def verify():
    
   
    with open(dbcrd, 'w') as f: 
        f.write(E1.get())
        f.write('\n')
        f.write(E2.get())
        f.write('\n')
        f.write(E3.get()) 
        f.close()
    
    with open(dbcrd) as f:
        data = f.readlines() 
        uname = data[0].rstrip() 
        pword = data[1].rstrip()
        lchst = data[2].rstrip()
   
    chk = mysql.connector.connect(host = lchst,user = uname,passwd = pword)
    chk1 = chk.is_connected()
    chk.close()
    if chk1 == True:
            a = tk.Tk()
            i = tk.Label(a,text = 'Verified :)')
            i.pack()
            a.after(2000, lambda: a.destroy())
            a.mainloop()
    elif chk1 != True:
    
           a = tk.Tk()
           i = tk.Label(a,text = 'Not Verified :(')
           i.pack()
           a.after(2000, lambda: a.destroy())
           a.mainloop()

def sql1():
    setL.destroy()
    sqlsetup()
def login():
    setSQL.destroy()
    global E1
    global E2
    global setL
    setL = tk.Tk()
    setL.title('Security')
    setL.geometry('450x250')
    heading = tk.Label(text = "Security", bg = "grey",width = '43', height = "1", font = ("Lucida Handwriting", 13))

    L1 = tk.Label(setL, text='Enter Your User Name:')
    L2 = tk.Label(setL, text = 'Enter your Password:')
    E1 = tk.Entry(setL)
    E2 = tk.Entry(setL,show = '*')
    B1 = tk.Button(setL,text = 'Insert',command = condition)
    B2 = tk.Button(setL,text = 'Setup SQL',command = sql1)
   
    heading.grid(row=0, column=0, columnspan=8)
    E1.grid(row =1 , column =2,padx = 10, pady=10 )
    E2.grid(row =2 , column =2,padx = 10, pady=10 )
    L1.grid(row =1, column =1 ,padx = 10, pady=10)
    L2.grid(row =2 , column =1,padx = 10, pady=10 )
    B1.grid(row = 3,column = 2,padx = 10, pady=10)
    B2.grid(row = 4,column = 2,padx = 10, pady=10)
    
    setL.mainloop()
    
def condition():
     
     
     if E1.get() == '':
        tk.messagebox.showerror(title = 'NO user name entered',message = 'ERror you did not enter the name')
     if E2.get() == '':
        tk.messagebox.showerror(title = 'NO password entered',message = 'ERror you did not enter the password')
     
     else:
         insert2()
        
def insert2():
    
    with open(File, 'w') as f: 
        f.write(E1.get())
        f.write('\n')
        f.write(E2.get()) 
        f.close()
    
    if os.path.isfile(File):
        Dis1 = tk.Tk()
        Dis1.geometry('150x50')
        Dis1.title('Login Success')
        i = tk.Label(Dis1,text = 'Credetials inserted :)')
        i.pack()
        Dis1.after(2000, lambda: Dis1.destroy())
        Dis1.mainloop()
        
    else:
        Dis1 = tk.Tk()
        L1= tk.Label(Dis1,text = 'Error,The credentials couldnot be inserted')
        L1.pack()
        Dis1.mainloop()

welcome.run()
ins()


def sql1():
    setL.destroy()
    sqlsetup()
    sucess()
def sucess():
    messagebox.showinfo('Success','The Setup Was complete, To start the program ,open Menu')
