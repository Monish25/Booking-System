import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk,Image

def rkill():
    a.destroy()
    a1.destroy()
def cash():
    global a
    a = tk.Tk()
    
    n = tk.Label(a,text = 'Enter Amount of cash:')
    e = tk.Entry(a)
    b = tk.Button(a,text = 'Ok',command = rkill)
    n.grid(column = 1,row = 1)
    e.grid(column = 2,row = 1)
    b.grid(column = 2 ,row = 3)

    a.mainloop()

 
def visa():
    global e
    global a
    a = tk.Tk()
    
    n = tk.Label(a,text = 'Enter Visa Number:')
    e = tk.Entry(a)
    b = tk.Button(a,text = 'Ok',command = vck)
    n.grid(column = 1,row = 1)
    e.grid(column = 2,row = 1)
    b.grid(column = 2 ,row = 3)

    a.mainloop()
    
def vck():
    a = e.get()
    if len(a) != 12:
        messagebox.showinfo('Error','Enter visa card properly')
    else:
        rkill()
def paytm():
    global a
    a = tk.Tk()
    L1 = tk.Label(a,text = 'Paytm Code : 46T55FV2R')
    b = tk.Button(a,text = 'Ok',command = rkill)
    L1.pack()
    b.pack()
    
    a.mainloop()

def NEFT():
    global a
    a = tk.Tk()
    L1 = tk.Label(a,text = 'IFSC CODE : S2SWd8fE5ee4W')
    L1.pack()
    B1 = tk.Button(a,text = 'Ok',command = rkill)
    B1.pack()
    a.mainloop()


a1 = tk.Tk()
a1.geometry('500x300')
a1.title('Payment')
L1=tk.Label(a1,text='PAYMENT',width='43',bg='grey',height='1',font=("Lucida Handwriting",13))
B1=tk.Button(a1,text='Cash',width=12,height=1,command = cash)
B2=tk.Button(a1,text='VISA',width=12,height=1,command = visa)
B3=tk.Button(a1,text='Paytm',width=12,height=1,command = paytm)
B4=tk.Button(a1,text='NEFT',width=12,height=1,command = NEFT)
B5=tk.Button(a1,text='Exit',width=12,height=1,command=a1.destroy) 



L1.grid(column=0,row=0,columnspan=6)
B1.grid(column=1,row=1 ,padx=5,pady=10)
B2.grid(column=3,row=1 ,padx=5,pady=10)
B3.grid(column=1,row=2,padx=5,pady=10)
B4.grid(column=3,row=2,padx=5,pady=10)
B5.grid(column=2,row=4,padx=5,pady=10)


a1.mainloop()
