import tkinter as tk
from PIL import ImageTk,Image
def run():
    Wc = tk.Tk()
    Wc.title('Setup')
    i1 = ImageTk.PhotoImage(file = 'logo.png')
    I1 = tk.Label(Wc,image = i1)
    I1.pack()
    Wc.after(2000, lambda: Wc.destroy())
    Wc.mainloop()
