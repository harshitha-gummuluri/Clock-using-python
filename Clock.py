from tkinter import *
from tkinter.ttk import *

from time import strftime

root=Tk()
root.title("Clock")


def time():
    string=strftime('%H:%M:%S %p %b,%A')
    label.config(text=string)
    label.after(1000,time)
    
label=Label(root,font=("calibri",80),background ="white",foreground ="black")
label.pack(anchor='center')
time()


mainloop()
    
