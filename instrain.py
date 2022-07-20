import tkinter as tk
from tkinter import messagebox
import mysql.connector
dbcrd = 'db.WDC'
with open(dbcrd) as f:
     data = f.readlines() 
     uname = data[0].rstrip() 
     pword = data[1].rstrip()
     lchst = data[2].rstrip()
def insert():
    a = e1.get()
    b = e2.get()
    c = e3.get()
    d = e4.get()
    e = e5.get()
    f = e6.get()
    g = e7.get()
    ins1(a,b,c,d,e,f,g)

def ins1(T_No, T_Name, T_Board, T_Dest,T_Dt,T_Fare,T_Dept):
    try:
        SQL = mysql.connector.connect(host = lchst,user = uname,passwd = pword,database = 'booking')
         
        cursor = SQL.cursor()
        sql_insert_query = """ INSERT INTO `rail`
                          (`T_No`, `T_Name`, `T_Board`, `T_Dest`,`T_Dt`,`T_Fare`,`T_Dept`) VALUES (%s,%s,%s,%s,%s,%s,%s)"""
        insert_tuple = (T_No, T_Name, T_Board, T_Dest,T_Dt,T_Fare,T_Dept)
        cursor.execute(sql_insert_query, insert_tuple)
        SQL.commit()
        messagebox.showinfo('Success',"Record inserted successfully into Booking Database RAIL Table")
        SQL.close()
            
    except:
        messagebox.showerror('Failure',"There was an Unexpected error that came, Check Your Information or The mySQl Connection")
            
  
  
    

global e1
global e2
global e3
global e4
global e5
global e6
global e7
a = tk.Tk()
a.geometry('250x250')
e1 = tk.Entry(a)
e2 = tk.Entry(a)
e3 = tk.Entry(a)
e4 = tk.Entry(a)
e5 = tk.Entry(a)
e6 = tk.Entry(a)
e7 = tk.Entry(a)
l1 = tk.Label(a,text = 'Train No')
l2 = tk.Label(a,text = 'Train Name')
l3 = tk.Label(a,text = 'Train Boarding')
l4 = tk.Label(a,text = 'Train Destination')
l5 = tk.Label(a,text = 'Train Distance')
l6 = tk.Label(a,text = 'Train Fare')
l7 = tk.Label(a,text = 'Train Departure')

b1 = tk.Button(a, text = 'insert',command = insert)
e1.grid(column = 2 , row = 1)
e2.grid(column = 2 , row = 2)
e3.grid(column = 2 , row = 3)
e4.grid(column = 2 , row = 4)
e5.grid(column = 2 , row = 5)
e6.grid(column = 2 , row = 6)
e7.grid(column = 2 , row = 7)
l1.grid(column = 1 , row = 1)
l2.grid(column = 1 , row = 2)
l3.grid(column = 1 , row = 3)
l4.grid(column = 1 , row = 4)
l5.grid(column = 1 , row = 5)
l6.grid(column = 1 , row = 6)
l7.grid(column = 1 , row = 7)

b1.grid(column = 2 , row = 8)
a.mainloop()
    


