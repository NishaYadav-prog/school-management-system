
import os

from tkinter import *
from tkinter import ttk
import time
from tkinter import messagebox
from subprocess import call
from PIL import Image, ImageTk
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
def click_loginn():
    call(["python", "smsafterlogin.py"])



class SCHOOL_LOGIN_SYSTEM:
    def __init__(self):
        root = Tk()
        root.geometry("998x600+250+50")
        root.title("school login system")
        root.configure(background="grey")
        root.configure(highlightbackground="#ffffff")
        root.configure(highlightcolor="#ffffff")
        root.resizable(0,0)
        
        self.menubar = Menu(root,font=("comic sans MS",9,"bold"))
        root.configure(menu = self.menubar)
        fileMenu=Menu(self.menubar,tearoff=0)
        
        self.menubar.add_cascade(label="  about us ",menu=fileMenu)
        
    #It is used to add the separator line to the menu.===============================================================================================================
        fileMenu.add_command(label="vision & mission ahead",command=self.about_us)
        fileMenu.add_separator()
    # academics Menu===============================================================================================================================================
        academicsMenu=Menu(self.menubar)
        
        academicsMenu=Menu(self.menubar,tearoff=0)
        self.menubar.add_cascade(label="academics",menu=academicsMenu)

        academicsMenu.add_command(label="curriculum & prospectus",command=self.curriculum_prospectus)
        academicsMenu.add_command(label="learning clubs")
        academicsMenu.add_command(label="syllabus")
    #sport Menu===============================================================================================================================================
        sportMenu=Menu(self.menubar)
        sportMenu=Menu(self.menubar,tearoff=0)
        self.menubar.add_cascade(label="sports",menu=sportMenu)

        sportMenu.add_command(label="basket ball",command=self.basket_ball)
        sportMenu.add_command(label="football")
        sportMenu.add_command(label="cricket")
        sportMenu.add_command(label="badminton/tennis")
        sportMenu.add_command(label="several indoor/outdoor games")
    #event Menu----------------------------------------------------------------------------------------------------------------------------------------------------

        eventMenu=Menu(self.menubar)
        eventMenu=Menu(self.menubar,tearoff=0)
        self.menubar.add_cascade(label="events",menu=eventMenu)

        contactMenu=Menu(self.menubar)
        contactMenu=Menu(self.menubar,tearoff=0)               
        self.menubar.add_cascade(label="contact us",menu=contactMenu)

        eventMenu.add_command(label="cultural programs",command=self.SCHOOL_DRESS)
        eventMenu.add_command(label="freshers'party/farewell")
        eventMenu.add_command(label="ceremony")
        eventMenu.add_command(label="workshops/training programme")
        
        contactMenu.add_command(label="me",command=self.contact_us)
     # Frame1 ----------------------------------------------------------------------------------------------------------------------------------------------------------
        self.Frame1 = Frame(root)
        self.Frame1.place(relx=0.02, rely=0.03, relheight=0.94, relwidth=0.96)
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(background="#ffffff")
        self.Frame1.configure(highlightbackground="#ffffff")
        self.Frame1.configure(highlightcolor="black")
        self.Frame1.configure(width=925)

    # bgimage in frame 1--------------------------------------------------------------------------------------------------------------------------------------------------------  
        
        self.bg_pic1 = ImageTk.PhotoImage(file="education.jpg")
        bgl_lbl=Label(self.Frame1,image=self.bg_pic1).pack()
    # log in ---------------------------------------------------------------------------------------------------------------------------------------------------------
         
        self.uname=StringVar()
        self.pass_=StringVar()


        Label(text='Username',font=("comic sans MS",18,"bold")).place(relx=0.12, rely=0.55, height=50, width=150)
        self.username=Entry(font=("comic sans MS",18),foreground="blue",textvariable=self.uname)
        self.username.place(relx=0.30, rely=0.55, height=50, width=300)

        Label(text='Password',font=("comic sans MS",18,"bold")).place(relx=0.12, rely=0.65, height=50, width=150)
        self.password=Entry(show='*',font=("comic sans MS",18),foreground="blue",textvariable=self.pass_)
        self.password.place(relx=0.30, rely=0.65, height=50, width=300)

        Label(text='PLEASE PRESS TWO TIMES LOGIN BUTTON  AFTER ENTER PASSWORD AND NAME',font=("comic sans MS",10,"bold")).place(relx=0.12, rely=0.89, height=45, width=570)


     # buttonss in frame 1 --------------------------------------------------------------------------------------------------------------------------------------------
        self.loginn=Button(self.Frame1,text="LOGIN",width=556,bg="#d9d9d9",font=("comic sans MS",14,"bold"),command=self.login).place(x=275,y=428,width=150,height=49)
      

        self.loginn=Button(self.Frame1,text="EXIST",width=556,bg="#d9d9d9",font=("comic sans MS",14,"bold"),command=quit).place(x=426,y=428,width=150,height=49)
        self.shclfee=Button(self.Frame1,text="SCHOOL FEE DETAIL",width=556,bg="#d9d9d9",font=("comic sans MS",14,"bold"),command=self.SCHOOL_FEE_DETAIL).place(x=670,y=480,width=250,height=49)
        self.RR=Button(self.Frame1,text="RULE RAGULATION",width=556,bg="#d9d9d9",font=("comic sans MS",14,"bold"),command=self.RULE_RAGULATION).place(x=670,y=390,width=250,height=49)       
        self.DRESS=Button(self.Frame1,text="DRESS",width=556,bg="#d9d9d9",font=("comic sans MS",14,"bold"),command=self.SCHOOL_DRESS).place(x=670,y=310,width=250,height=49)       
        self.SF=Button(self.Frame1,text="SCHOOL FACILITIES",width=556,bg="#d9d9d9",font=("comic sans MS",14,"bold"),command=self.SCHOOL_FCILITIES).place(x=670,y=220,width=250,height=49)       

     
      

       
        root.mainloop()
# commands===========================================================================================================================================================
    def SCHOOL_FCILITIES(self):
            SCHOOL_FCILITIES= Toplevel(self.Frame1)
            SCHOOL_FCILITIES.configure(background="grey")
            SCHOOL_FCILITIES.title("school facilities")
            SCHOOL_FCILITIES.geometry("998x600+250+50")
            Label(SCHOOL_FCILITIES, text="SCHOOL FACILITIES",font=("comic sans MS",20,"bold"),background="grey").pack()
            Label(SCHOOL_FCILITIES, text="").pack()
            self.pic = ImageTk.PhotoImage(file="imagesOX8FUG9U.jpg")
            labelimage=Label(
            SCHOOL_FCILITIES,image=self.pic,fg="green",font=("comic sans MS",30,"bold"),relief=RIDGE,background="#ffffff",bd=4)
            labelimage.place(x=27,y=40,width=950,height=540)
    def SCHOOL_DRESS(self):
        SCHOOL_DRESS= Toplevel(self.Frame1)
        SCHOOL_DRESS.title("school facilities")
        SCHOOL_DRESS.geometry("998x600+250+50")
        Label(SCHOOL_DRESS, text="SCHOOL DRESS",font=("comic sans MS",20,"bold")).pack()
        Label(SCHOOL_DRESS, text="").pack()
        self.pic = ImageTk.PhotoImage(file="4.jpg")
        labelimage=Label(
            SCHOOL_DRESS,image=self.pic,fg="green",font=("comic sans MS",30,"bold"),relief=RIDGE,background="#ffffff",bd=4)
        labelimage.place(x=27,y=40,width=950,height=540)

        
    def RULE_RAGULATION(self):
        RULE_RAGULATION= Toplevel(self.Frame1)
        RULE_RAGULATION.title("school facilities")
        RULE_RAGULATION.geometry("998x600+250+50")
        Label(RULE_RAGULATION, text="RULE RAGULATION",font=("comic sans MS",20,"bold")).pack()
        Label(RULE_RAGULATION, text="").pack()

        self.pic = ImageTk.PhotoImage(file="imagesOX8FUG9U.jpg")
        labelimage=Label(
            RULE_RAGULATION,image=self.pic,fg="green",font=("comic sans MS",30,"bold"),relief=RIDGE,background="#ffffff",bd=4)
        labelimage.place(x=27,y=40,width=950,height=540)

    def SCHOOL_FEE_DETAIL(self):
        SCHOOL_FEE_DETAIL= Toplevel(self.Frame1)
        SCHOOL_FEE_DETAIL.title("school facilities")
        SCHOOL_FEE_DETAIL.geometry("998x600+250+50")
        Label(SCHOOL_FEE_DETAIL, text="SCHOOL FEE DETAIL",font=("comic sans MS",20,"bold")).pack()
        Label(SCHOOL_FEE_DETAIL, text="").pack()
        self.pic = ImageTk.PhotoImage(file="fee detail.png")
        labelimage=Label(
            SCHOOL_FEE_DETAIL,image=self.pic,fg="green",font=("comic sans MS",30,"bold"),relief=RIDGE,background="#ffffff",bd=4)
        labelimage.place(x=27,y=40,width=950,height=540)
    def about_us(self):
        about_us= Toplevel(self.Frame1)
        about_us.configure(background="grey")
        about_us.title("ABOUT US")
        about_us.geometry("1000x700+0+0")
        about_us.resizable(0,0)
        self.pic = ImageTk.PhotoImage(file="about us.jpg")
        labelimage=Label(
            about_us,image=self.pic,fg="green",font=("comic sans MS",30,"bold"),relief=RIDGE,background="#ffffff",bd=4)
        labelimage.place(x=27,y=33,width=950,height=650)     
      
    def curriculum_prospectus(self):
        curriculum_prospectus= Toplevel(self.Frame1)
        curriculum_prospectus.title("curriculum_prospectus")
        curriculum_prospectus.geometry("998x600+250+50")
        Label(curriculum_prospectus, text="SCHOOL FEE DETAIL",font=("comic sans MS",20,"bold")).pack()
        Label(curriculum_prospectus, text="").pack()
        self.pic = ImageTk.PhotoImage(file="fee detail.png")
        labelimage=Label(
            curriculum_prospectus,image=self.pic,fg="green",font=("comic sans MS",30,"bold"),relief=RIDGE,background="#ffffff",bd=4)
        labelimage.place(x=27,y=40,width=950,height=580)       
    def basket_ball(self):
        curriculum_prospectus= Toplevel(self.Frame1)
        curriculum_prospectus.title("curriculum_prospectus")
        curriculum_prospectus.geometry("998x600+250+50")
        Label(curriculum_prospectus, text="BASKET BALL",font=("comic sans MS",20,"bold")).pack()
        Label(curriculum_prospectus, text="").pack()
        self.pic = ImageTk.PhotoImage(file="football.jpg")
        labelimage=Label(
            curriculum_prospectus,image=self.pic,fg="green",font=("comic sans MS",30,"bold"),relief=RIDGE,background="#ffffff",bd=4)
        labelimage.place(x=27,y=40,width=950,height=550)
    def contact_us(self):
        curriculum_prospectus= Toplevel(self.Frame1)
        curriculum_prospectus.title("curriculum_prospectus")
        curriculum_prospectus.geometry("998x600+250+50")
        self.bg_pic2 = ImageTk.PhotoImage(file="580b57fbd9996e24bc43bd30.png")
        bgl_lbl=Label(curriculum_prospectus,image=self.bg_pic2).pack()
  
        Label(text='Username',font=("comic sans MS",18,"bold"),foreground="blue").place(relx=0.12, rely=0.50, height=50, width=150)

    def login(self):
     
        if self.uname.get()=="nisha"  and self.pass_.get()=="nisha":
            self.nisha()
            
           
        else:
            messagebox.showerror("error","plz enter valid username or password ")
            self.asdf()
    # progress bar ------------------------------------------------------------------------------------------------------------------------------------------------
    def nisha(self):
        self.nisha=Frame(self.Frame1)
        self.nisha.place(relx=0.185, rely=0.76, height=96, width=450)
        self.bg_pic2 = ImageTk.PhotoImage(file="bar.png")
        bgl_lbl=Label(self.nisha,image=self.bg_pic2).pack()
        
        self.progressBar()




    def progressBar(self):
        self.button14 = Button(self.nisha, text = "LOGIN",font=("comic sans MS",15,"bold"),activebackground="#d9d9d9",background="#d9d9d9", command = self.run_progressbar)
        self.button14.place(relx=0.225, rely=0.01, height=50, width=142)

        self.button23 = Button(self.nisha, text = "EXIST",font=("comic sans MS",15,"bold"),activebackground="#d9d9d9",background="#d9d9d9",
                               command = quit)
        self.button23.place(relx=0.57, rely=0.01, height=50, width=142)

        self.progress_bar = ttk.Progressbar(self.nisha, orient = 'horizontal', length = 286, mode = 'determinate')
        self.progress_bar.place(relx=0.01, rely=0.6, height=30, width=430)


    def run_progressbar(self):
        self.progress_bar["maximum"] = 100

        for i in range(101):
            time.sleep(0.05)
            self.progress_bar["value"] = i
            self.progress_bar.update()
            
        self.progress_bar["value"] = 0
        click_loginn()
        self.asdf()
        self.nisha.destroy()
       

    def asdf(self):
       self.uname.set("")
       self.pass_.set("")
       

if __name__ == '__main__':
    login=SCHOOL_LOGIN_SYSTEM()


