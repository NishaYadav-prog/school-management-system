
from tkinter import *
from tkinter import  ttk
import pymysql
import random
import os
from PIL import Image, ImageTk
import pickle
import sys
import os
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
        self.root.geometry("1350x700+0+0")
        
       #To insert Menu in Window
        main_menu=Menu(self.root)
        self.root.config(menu=main_menu)

        #Create File Menu
        fileMenu=Menu(main_menu,tearoff=0)
        #add_command is used to add the Menu items to the Menu
        fileMenu.add_command(label="Log out",command=self.login_sucess)
        

        #add_cascade is used to create a hierarchical Menu to the parent Menu by associating the given menu to the parent menu.
        main_menu.add_cascade(label="  File  ",menu=fileMenu)

        
        fileMenu.add_separator()

        title=Label(self.root,text="WELCOME TO SCHOOL MANAGEMENT SYSTEM",font=("algerian",32,"bold"),bg="sky blue",fg="black")
        title.pack(side=TOP,fill=X)
        self.bg_pic1 = ImageTk.PhotoImage(file="121.jpg")
        bgl_lbl=Label(self.root,image=self.bg_pic1).pack()
        #********** All variable*********
        self.roll_no_var=StringVar()
        self.name_var=StringVar()
        self.email_var=StringVar()
        self.gender_var=StringVar()
        self.contact_var=StringVar()
        self.dob_var=StringVar()
        
        
        
        self.search_by=StringVar()
        self.search_txt=StringVar()
        #**************Manage Frame**********************
  
        
        lbl_roll=Label(self.root,text="Roll",bg="pink",fg="black",font=("times new roman",15,"bold"))
        lbl_roll.place(x=30,y=100,width=100,height=40)
  
        txt_roll=Entry(self.root,textvariable=self.roll_no_var,font=("times new roman",10,"bold"),bd=5,relief=GROOVE)
        txt_roll.place(x=200,y=100,width=200,height=40)
        
        lbl_name=Label(self.root,text="Name",bg="pink",fg="black",font=("times new roman",15,"bold"))
        lbl_name.place(x=30,y=160,width=100,height=40)
        
        txt_name=Entry(self.root,textvariable=self.name_var,font=("times new roman",10,"bold"),bd=5,relief=GROOVE)
        txt_name.place(x=200,y=160,width=200,height=40)

        lbl_email=Label(self.root,text="Class",bg="pink",fg="black",font=("times new roman",15,"bold"))
        lbl_email.place(x=30,y=220,width=100,height=40)
        
        txt_email=Entry(self.root,textvariable=self.email_var,font=("times new roman",10,"bold"),bd=5,relief=GROOVE)
        txt_email.place(x=200,y=220,width=200,height=40)
        
        lbl_gender=Label(self.root,text="Gender",bg="pink",fg="black",font=("times new roman",15,"bold"))
        lbl_gender.place(x=30,y=280,width=100,height=40)

        combo_gender=ttk.Combobox(self.root,textvariable=self.gender_var,font=("times new roman",9,"bold"),state="readonly")
        combo_gender['values']=("Male","Female","Other")
        combo_gender.place(x=200,y=280,width=200,height=40)
     

        lbl_contact=Label(self.root,text="Contact",bg="pink",fg="black",font=("times new roman",15,"bold"))
        lbl_contact.place(x=450,y=100,width=100,height=40)
        
        txt_contact=Entry(self.root,textvariable=self.contact_var,font=("times new roman",10,"bold"),bd=5,relief=GROOVE)
        txt_contact.place(x=600,y=100,width=200,height=40)

        lbl_dob=Label(self.root,text="D.O.B.",bg="pink",fg="black",font=("times new roman",15,"bold"))
        lbl_dob.place(x=450,y=220,width=100,height=40)
        
        txt_dob=Entry(self.root,textvariable=self.dob_var,font=("times new roman",10,"bold"),bd=5,relief=GROOVE)
        txt_dob.place(x=600,y=220,width=200,height=40)

        lbl_addr=Label(self.root,text="Address",bg="pink",fg="black",font=("times new roman",15,"bold"))
        lbl_addr.place(x=450,y=160,width=100,height=40)

        self.txt_addr=Text(self.root,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        self.txt_addr.place(x=600,y=160,width=200,height=40)


        #*******button Frame*******
        addbutton=Button(self.root,text="Add",width=8,command=self.add_student).place(x=1200,y=100,width=100,height=40)
        updatebutton=Button(self.root,text="Update",width=8,command=self.update_data).place(x=1200,y=160,width=100,height=40)
        deletebutton=Button(self.root,text="Delete",width=8,command=self.delete_data).place(x=1200,y=220,width=100,height=40)
        clearbutton=Button(self.root,text="Clear",width=8,command=self.clear).place(x=1200,y=280,width=100,height=40)
        
        #**************Detail Frame**********************
       
        self.pic = ImageTk.PhotoImage(file="adminicon.png")#(for image in main(app) page)
       
        labelimage=Label(
            self.root,text="ALWAYS BE HAPPY \n AND DO YOUR BEST",image=self.pic,fg="green",font=("comic sans MS",30,"bold"),relief=RIDGE,background="#ffffff",bd=1)
        labelimage.place(x=890,y=100,width=250,height=160)

       
        lbl_search=Label(self.root,text="Search By",bg="pink",fg="black",font=("times new roman",15,"bold"))
        lbl_search.place(x=450,y=280,width=100,height=40)
        
        combo_search=ttk.Combobox(self.root,width=10,textvariable=self.search_by,font=("times new roman",10,"bold"),state="readonly")
        combo_search['values']=("roll_no","name","contact")
        combo_search.place(x=600,y=280,width=100,height=40)

        txt_search=Entry(self.root,textvariable=self.search_txt,font=("times new roman",10,"bold"),bd=4,relief=GROOVE)
        txt_search.place(x=750,y=280,width=130,height=40)
        searchbtn=Button(self.root,text="Search",width=7,pady=3,command=self.search_data).place(x=900,y=280,width=100,height=40)
        showbtn=Button(self.root,text="Show All",width=8,pady=3,command=self.fetch_data).place(x=1050,y=280,width=100,height=40)
        
        #**************Table Frame****************
             
        Table_frame=Frame(self.root,bd=4,relief=RIDGE,bg="pink")
        Table_frame.place(x=450,y=350,width=850,height=320)
        scroll_x=Scrollbar(Table_frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(Table_frame,orient=VERTICAL)
        self.Student_table=ttk.Treeview(Table_frame,columns=("roll","name","email","contact","gender","dob","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Student_table.xview)
        scroll_y.config(command=self.Student_table.yview)

        
        self.Student_table.heading("roll",text="Roll No")
        self.Student_table.heading("name",text="Name")
        self.Student_table.heading("email",text="Class")
        self.Student_table.heading("gender",text="Gender")
        self.Student_table.heading("contact",text="Contact")
        self.Student_table.heading("dob",text="D.O.B.")
        self.Student_table.heading("address",text="Address")

        self.Student_table['show']='headings'
        self.Student_table.column("roll",width=60)
        self.Student_table.column("name",width=110)
        self.Student_table.column("email",width=110)
        self.Student_table.column("gender",width=110)
        self.Student_table.column("contact",width=110)
        self.Student_table.column("dob",width=110)
        self.Student_table.column("address",width=110)
        self.Student_table.pack(fill=BOTH,expand=1)
        self.Student_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

        
######################## def function#######################################

    def add_student(self):
        
            con=pymysql.connect(host='localhost',user='root',database='stm4')
            cur=con.cursor()
            cur.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s);",(
                self.roll_no_var.get(),
                self.name_var.get(),
                self.email_var.get(),
                self.gender_var.get(),
                self.contact_var.get(),
                self.dob_var.get(),
                self.txt_addr.get('1.0',END)
            ))
            con.commit()
            
            self.fetch_data()
            con.close()
    def fetch_data(self):
        con=pymysql.connect(host='localhost',user='root',database='stm4')
        cur=con.cursor()
        cur.execute("select * from students")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('',END,values=row)
                con.commit()
        con.close()
    def clear(self):
        self.roll_no_var.set("")
        self.name_var.set("")
        self.email_var.set("")
        self.contact_var.set("")
        self.gender_var.set("")
        self.dob_var.set("")
        self.txt_addr.delete("1.0",END)

    def get_cursor(self,ev):
        cursr_row=self.Student_table.focus()
        contents=self.Student_table.item(cursr_row)
        row=contents['values']
        self.roll_no_var.set(row[0])
        self.name_var.set(row[1])
        self.email_var.set(row[2])
        self.contact_var.set(row[3])
        self.gender_var.set(row[4])
        self.dob_var.set(row[5])
        self.txt_addr.delete("1.0",END)
        self.txt_addr.insert(END,row[6])
    def update_data(self):
        con=pymysql.connect(host='localhost',user='root',database='stm4')
        cur=con.cursor()
        cur.execute("update students set name=%s,email=%s,gender=%s,contact=%s,dob=%s,addr=%s where roll_no=%s ;",(
                self.name_var.get(),
                self.email_var.get(),
                self.gender_var.get(),
                self.contact_var.get(),
                self.dob_var.get(),
                self.txt_addr.get('1.0',END),
                self.roll_no_var.get()
            ))
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()
    def delete_data(self):
        con=pymysql.connect(host='localhost',user='root',database='stm4')
        cur=con.cursor()
        cur.execute("delete from students where roll_no=%s;",self.roll_no_var.get())
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()
    def login_sucess(self):
        global login_success_screen
        login_success_screen = Toplevel(self.root)
        login_success_screen.title("Success")
        login_success_screen.geometry("400x150")
        Label(login_success_screen, text="Logout Success",font=("times new roman",15,"bold")).pack()
        Button(login_success_screen, text="OK",font=("times new roman",15,"bold"), command=quit).pack()

    
    def search_data(self):
        con=pymysql.connect(host='localhost',user='root',database='stm4')
        cur=con.cursor()
        cur.execute("select * from students where "+str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%'")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('',END,values=row)
                con.commit()
        con.close()

    
root=Tk()   

ob=Student_system(root)
root.mainloop()

if __name__ == '__main__':
    school=Student_system()
