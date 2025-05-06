
from tkinter import *
from tkinter import  ttk
import pymysql
import random

import datetime 
import os
from PIL import Image, ImageTk
from tkinter import messagebox
import pickle
import sys
import os
import mysql.connector as sqltor
from subprocess import call

import sys

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


class Student_system:
   
    def __init__(self,root):
        self.root=root
        self.root.title("WELCOME TO  SCHOOL MANAGEMENT SYSTEM")
        self.root.geometry("720x500+250+50")

        #********** All variable*********
        self.roll_no_var=StringVar()
        self.name_var=StringVar()
        self.email_var=StringVar()
        self.gender_var=StringVar()
        self.contact_var=StringVar()
        self.dob_var=StringVar()
        self.father_var=StringVar()
        self.mother_var=StringVar()
        self.search_by=StringVar()
        self.search_txt=StringVar()
        #**************Manage Frame**********************
        global x3
        self.bg_pic1 = ImageTk.PhotoImage(file="gh.png")
        bgl_lbl=Label(self.root,image=self.bg_pic1).place(x=110,y=0,width=680,height=500)
        Table_frame=Frame(self.root,bd=4,relief=RIDGE,bg="white")
        Table_frame.place(x=50,y=100,width=330,height=350)
        lb1=Label(self.root,text=" STUDENT ID",bg="white",fg="black",font=("times new roman",15,"bold"))
        lb1.place(x=80,y=300,width=120,height=40)
        x3=Entry(self.root,font=("times new roman",10,"bold"),bd=4,relief=GROOVE)
        x3.place(x=220,y=300,width=130,height=40)
        searchbtn=Button(self.root,text="Login",width=7,bg="white",font=("times new roman",15,"bold"),bd=0,pady=3,command=self.modify).place(x=80,y=380,width=100,height=40)
        existbtn=Button(self.root,text="EXIST",width=7,bg="white",font=("times new roman",15,"bold"),bd=0,pady=3,command=quit).place(x=220,y=380,width=100,height=40)
        fbtn=Button(self.root,text="Forget Password ?",width=7,bg="white",fg="red",font=("times new roman",15,"bold"),bd=0,pady=3,command=self.er).place(x=190,y=350,width=180,height=30)
        lbl2=Button(self.root,text="STUDENT LOGIN",width=7,bg="white",fg="blue",font=("times new roman",15,"bold"),bd=0,pady=3).place(x=120,y=250,width=180,height=30)
        self.pic = ImageTk.PhotoImage(file="icon.png")#(for image in main(app) page)
        labelimage=Label(
            self.root,text="ALWAYS BE HAPPY \n AND DO YOUR BEST",image=self.pic,fg="green",font=("comic sans MS",30,"bold"),relief=RIDGE,background="#ffffff",bd=0)
        labelimage.place(x=130,y=120,width=170,height=120)
    

    def modify(self):
        global x3,x4
        p1=x3.get()
        con=pymysql.connect(host='localhost',user='root',database='stm4')
        cur=con.cursor()
        
        cur.execute('select * from students where roll_no=(%s)',(p1,))
        dat=cur.fetchall()
        a=[]
        for i in dat:
            a.append(i)
        if len(a)==0:
            messagebox.showerror("ERROR", "NO DATA FOUND!!")
        else:
            root6=Toplevel(self.root)
            frame=Frame(root6,height=300,width=500,relief=RIDGE,bg="white")
            frame.pack()
        
           
            """self.bg_pic2 = ImageTk.PhotoImage(file="4.jpg")
            bgl_lbl=Label(frame,image=self.bg_pic2,bd=1).place(x=180,y=30,width=130,height=90)"""
            
            self.pic9 = ImageTk.PhotoImage(file="icon.png")#(for image in main(app) page)
        
            # labelimage=Label(
            #     frame,image=self.pic9,fg="green",font=("comic sans MS",30,"bold"),relief=RIDGE,background="#ffffff",bd=3)
            # labelimage.place(x=320,y=70,width=140,height=120)

          
            for i in dat:
                lb1=Label(root6,text=" STUDENT DETAIL",bg="white",fg="black",font=("times new roman",25,"bold")).place(x=50,y=20)
                lb1=Label(root6,text=" STUDENT PHOTO",bg="white",fg="black",font=("times new roman",15,"bold")).place(x=300,y=200)
                
                name=Label(root6,bg="white",fg="red",text='NAME:-',font=("times new roman",15,"bold"))
                name.place(x=50,y=60)
                name1=Label(root6,bg="white",fg="blue",text=i[1],font=("times new roman",15,"bold"))
                name1.place(x=150,y=60)

                age=Label(root6,bg="white",fg="red",text='CLASS:-',font=("times new roman",15,"bold"))
                age.place(x=50,y=90)
                age1=Label(root6,bg="white",fg="blue",text=i[2],font=("times new roman",15,"bold"))
                age1.place(x=150,y=90)

                gen=Label(root6,bg="white",fg="red",text='CONTACT:-',font=("times new roman",15,"bold"))
                gen.place(x=50,y=120)
                gen1=Label(root6,bg="white",fg="blue",text=i[3],font=("times new roman",15,"bold"))
                gen1.place(x=170,y=120)

                pho=Label(root6,bg="white",fg="red",text='GENDER:-',font=("times new roman",15,"bold"))
                pho.place(x=50,y=150)
                pho1=Label(root6,bg="white",fg="blue",text=i[4],font=("times new roman",15,"bold"))
                pho1.place(x=180,y=150)

                bg=Label(root6,bg="white",fg="red",text='DOB:-',font=("times new roman",15,"bold"))
                bg.place(x=50,y=180)
                bg1=Label(root6,bg="white",fg="blue",text=i[5],font=("times new roman",15,"bold"))
                bg1.place(x=150,y=180)

                dob=Label(root6,bg="white",fg="red",text='ADDRESS:-',font=("times new roman",15,"bold"))
                dob.place(x=50,y=210)
                dob1=Label(root6,bg="white",fg="blue",text=i[6],font=("times new roman",15,"bold"))
                dob1.place(x=150,y=210)
                
            
          
            root6.resizable(False,False)
            root6.mainloop()
    def er(self):
        messagebox.showerror("ERROR", "PLEASE CONTECT WITH ADMIN")

      
       
    def login_sucess(self):
        global login_success_screen
        login_success_screen = Toplevel(self.root)
        login_success_screen.title("Success")
        login_success_screen.geometry("400x150")
        Label(login_success_screen, text="Logout Success",font=("times new roman",15,"bold")).pack()
        Button(login_success_screen, text="OK",font=("times new roman",15,"bold"), command=quit).pack()
 

    


    
root=Tk()   

ob=Student_system(root)
root.mainloop()

if __name__ == '__main__':
    school=Student_system()
