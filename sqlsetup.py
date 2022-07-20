import tkinter as tk
from tkinter import messagebox
import mysql.connector
dbcrd = 'db.WDC'
with open(dbcrd) as f:
        data = f.readlines() 
        uname = data[0].rstrip() 
        pword = data[1].rstrip()
        lchst = data[2].rstrip()
def sql1():
    try:
        SQLC = mysql.connector.connect(host = lchst,user = uname,passwd = pword)
        cfg = SQLC.cursor()
        cfg.execute('CREATE DATABASE booking')
        SQLC.commit()
        SQLC.close()
        sql2()
    except:
        messagebox.showinfo('Error', 'The data cannot be inserted ,\ncheck your SQL server')
def sql2():
    try:
        SQLC = mysql.connector.connect(host = lchst,user = uname,passwd = pword,database = 'booking')
        cfg = SQLC.cursor()
        cfg.execute("CREATE TABLE bus (B_No int(11)  PRIMARY KEY,B_Name char (255),B_Board char (255),B_Dest char(11),B_Dt int(11),B_Fare int(11),B_Dept char(5))")
        cfg.execute("CREATE TABLE flight (F_No char(255) PRIMARY KEY,F_Name char (255),F_Board char (255),F_Dest char(11),F_Dt int(11),F_Fare int(11),F_Dept char(5))")
        cfg.execute("CREATE TABLE rail (T_No int(11) PRIMARY KEY,T_Name char (255),T_Board char (255),T_Dest char(11),T_Dt int(11),T_Fare int(11),T_Dept char(5))")
        SQLC.commit()
        messagebox.showinfo('success','The Database along with the table has been created\n The Data has to be Entered by Yourself')
    except:
        messagebox.showinfo('Error','The data cannot be inserted check your SQL server')
D1 = tk.Tk()
D1.geometry('350x100')

L1 = tk.Label(D1,text = '\tWelcome to the SQL Setup,\n\t Make sure the SQL server is Running and\n\t This will configure the SQL Server\n\t To make the databases for inserting information')
B1 = tk.Button(D1,text = 'Configure',command = sql1)

L1.grid(column =1 ,row = 1)
B1.grid(column =1 ,row = 2)
D1.mainloop()    
