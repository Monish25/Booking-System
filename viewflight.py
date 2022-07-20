import tkinter as tk
import mysql.connector
import os
from tkinter import ttk
global E1
global E2
global tree
def next():
    os.system('flightdat.py')
    V1.destroy()
def collect1():
    a = E1.get()
    b = E2.get()
    collect2(a,b)
def collect2(a,b):
    
        dbcrd = 'db.WDC'
        with open(dbcrd) as f:
            data = f.readlines() 
            uname = data[0].rstrip() 
            pword = data[1].rstrip()
            lchst = data[2].rstrip()
   
        mySQLConnection = mysql.connector.connect(host = lchst,user = uname,passwd = pword,database = 'booking')
         
        cursor = mySQLConnection.cursor()
        sql_select_query = """select * from flight where F_Board = %s and F_Dest = %s"""
        cursor.execute(sql_select_query, (a,b,))
        record = cursor.fetchall()
        cursor.close()
        tree.delete(*tree.get_children())
        for row in record:
            
            tree.insert("", tk.END, values=row)
            
            
global V1
V1 = tk.Tk()
V1.title('View Flights')
V1.geometry('800x500')
L1 = tk.Label(V1,text = 'Enter Starting point')
L2 = tk.Label(V1,text = 'Enter Destination point')
E1 = tk.Entry(V1)
E2 = tk.Entry(V1)

tree = ttk.Treeview(V1,column=("column1", "column2", "column3","column4","column5","column6","column7"), show='headings',selectmode="extended")

tree.heading("#1", text="Flight No")
tree.heading("#2", text="Flight Name")
tree.heading("#3", text="Flight Boarding")
tree.heading("#4", text="Flight Destination")
tree.heading("#5", text="Flight Dist")
tree.heading("#6", text="Flight Fare")
tree.heading("#7", text="Flight Dept")


tree.column("#1",minwidth=0,width=60)
tree.column("#2",minwidth=0,width=95)
tree.column("#3",minwidth=0,width=95)
tree.column("#4",minwidth=0,width=105)
tree.column("#5",minwidth=0,width=65)
tree.column("#6",minwidth=0,width=85)
tree.column("#7",minwidth=0,width=70)
B3 = tk.Button(V1,text = 'Exit',command = V1.destroy)
B2 = tk.Button(V1,text = 'Book',command = next)
B1 = tk.Button(V1,text = 'Search',command = collect1)

L1.grid(column = 1,row = 1,padx=5,pady=10)
L2.grid(column = 1,row = 2,padx=5,pady=10)
tree.grid(column = 2,row = 4,padx=5,pady=10)
B1.grid(column = 2,row = 3,padx=5,pady=10)
E1.grid(column = 2,row = 1,padx=5,pady=10)
E2.grid(column = 2,row = 2,padx=5,pady=10)
B2.grid(column = 2,row = 6,padx=5,pady=10)
B3.grid(column = 2,row = 7,padx=5,pady=10)
V1.mainloop()





