import tkinter
from tkinter import *
import tkinter.messagebox as msg
from connection import Connect
import userLogin
import adminlogin

class main:
    def __init__(self):
        self.root = Tk()
        self.root.title('Welcome')
        self.root.geometry('800x800')
        self.root.configure(bg="#CFDBD5")

        self.mainlabel=tkinter.Label(self.root,text="Recipe System",font=('arial',28,'bold'), bg="#E8EDDF")
        self.mainlabel.pack(pady=20, ipadx=10, ipady=10)

        self.formframe = tkinter.Frame(self.root, bg="#E8EDDF")
        self.formframe.pack()

        self.btn = tkinter.Button(self.formframe, text="Admin", width=20, font=('arial',17), command=lambda:adminlogin.main(), bg="#E8EDDF",
                                  foreground="black")
        self.btn.grid(row=0,column=1,pady=20,padx=20)

        self.btn1 = tkinter.Button(self.formframe, text="User", width=20, font=('arial',17), command=lambda:userLogin.user(), bg="#E8EDDF",
                                  foreground="black")
        self.btn1.grid(row=0,column=2,pady=20,padx=20)

        self.root.mainloop()

x=main()