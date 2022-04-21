from tkinter import *
from tkinter import messagebox
import tkinter
import pyspeedtest
def one():
    speed=pyspeedtest.SpeedTest("www.google.com")
    a1=(str(speed.download())+"[Megabits per second]")
    messagebox.showinfo("Your download speed : ",a1)
root=Tk()
root.title("SpeedCheck")
root.config(bg="aqua")
root.geometry("500x250")
label1=Label(root,text="Internet Speed Checker", font=("Arial",30,"bold"),bg="pink").pack()
button1=Button(root,text="Click Here", font=("Arial",20,"bold"),bg="yellow",height=1,width=10,command=one).pack()

root.mainloop()
