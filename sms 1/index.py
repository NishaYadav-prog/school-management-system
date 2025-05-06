import os
from subprocess import call

import sys
from PIL import Image, ImageTk

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

def click_list():
    call(["python", "adminlogin.py"])

def click_mnbv():
    call(["python","studentlogin.py"])


class SCHOOL_LOGIN:
    def __init__(self):
        root = Tk()


        root.geometry("998x600+250+50")
        root.title("SMS")
        root.configure(background="#d9d9d9")
        root.configure(highlightbackground="#d9d9d9")
        root.configure(highlightcolor="black")
        root.resizable(0,0)



        self.menubar = Menu(root,font=("roman"),bg="gray",fg="black")
        root.configure(menu = self.menubar)
        ############## background image ###################
        self.bg_pic1 = ImageTk.PhotoImage(file="quote.jpg")
        bgl_lbl=Label(root,image=self.bg_pic1).pack()
        ################ image #######################
        self.pic = ImageTk.PhotoImage(file="admin.jpg")
     
        labelimage=Label(
            root,image=self.pic,fg="green",font=("comic sans MS",30,"bold"),relief=RIDGE,background="#ffffff",bd=1)
        labelimage.place(x=80,y=85,width=220,height=200)

        
        self.pic1 = ImageTk.PhotoImage(file="stu.jpg")
     
        labelimage=Label(
            root,image=self.pic1,fg="green",font=("comic sans MS",30,"bold"),relief=RIDGE,background="#ffffff",bd=1)
        labelimage.place(x=80,y=340,width=220,height=200)


        ################# buttons ########################
        self.Message =Label(root,text="WELCOME",bg="black",fg="white",font=("times new roman",30,"bold")).place(x=82,y=10,width=300,height=60)
        self.Button1 =Button(root,text="ADMIN LOGIN",width=556,bg="black",fg="white",font=("times new roman",20,"bold"),command=click_list).place(x=320,y=150,width=240,height=50)
        self.Button2 = Button(root,text="STUDENT LOGIN",width=556,bg="black",fg="white",font=("times new roman",20,"bold"),command=click_mnbv).place(x=320,y=400,width=240,height=50)
        self.Button3 =Button(root,text="EXIST",width=556,bg="black",fg="red",font=("times new roman",20,"bold"),command=quit).place(x=82,y=550,width=240,height=50)

        root.mainloop()


if __name__ == '__main__':
    GUUEST=SCHOOL_LOGIN()


