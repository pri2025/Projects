from tkinter import *
import tkinter.ttk as ttk
from PIL import Image, ImageTk
import tkinter.messagebox as msg
import customtkinter
from connection import Connect
from gtts import gTTS
import playsound
import threading
import os


class Main:
    def __init__(self,userid):
        self.userid = userid
        self.root = Toplevel()
        self.root.state('zoomed')
        self.root.configure(bg="#AD9BAA")

        self.label = Label(self.root, text="Recipe List", font=('', 28, 'bold'), bg='#CFCCD6')
        self.label.pack(pady=20)

        self.recipyFrame = customtkinter.CTkScrollableFrame(self.root, width=self.root.winfo_screenwidth(),
                                                            height=self.root.winfo_screenheight())
        self.recipyFrame.pack(pady=10)
        self.recipyFrame.columnconfigure(0)

        self.getRecipy()

        self.root.mainloop()

    def getRecipy(self):
        self.conn = Connect()
        self.cr = self.conn.cursor()

        q = f"SELECT * FROM recipe where image !=''"
        self.cr.execute(q)
        result = self.cr.fetchall()
        self.showRecipy(result)

    def showRecipy(self, recipes):
        for i in recipes:
            print(i[1])
            self.f = Frame(self.recipyFrame, width=self.root.winfo_screenwidth())
            self.f.pack(expand=True, fill='both')

            img = Image.open(fp=i[-1])
            img = img.resize((200, 200))
            imgTk = ImageTk.PhotoImage(image=img)
            self.l = Label(self.f, image=imgTk)
            self.l.image = imgTk
            self.l.grid(row=0, column=0, pady=10, padx=10)

            self.f1 = Frame(self.f)
            self.f1.grid(row=0, column=1, pady=10, padx=10)

            self.name = Label(self.f1, text=i[1], font=('', 14))
            self.name.pack(pady=10)
            self.duration = Label(self.f1, text=f"Duration(in min): {i[3]}", font=('', 12))
            self.duration.pack(pady=10)
            self.cat = Label(self.f1, text=f"Category: {i[5]}", font=('', 12))
            self.cat.pack(pady=10)

            self.btn = Button(self.f1, text="View More", font=('', 14), command=lambda r=i: self.playRecipy(r))
            self.btn.pack()

    def playRecipy(self, recipy):
        print(recipy)
        self.recipyid = recipy[0]
        self.root1 = Toplevel()
        name= recipy[1]
        self.root1.title('recipy')
        self.root1.geometry('800x800')


        self.label = Label(self.root1, text=name, font=('', 18, 'bold'))
        self.label.pack(pady=10)

        self.scroll = customtkinter.CTkScrollableFrame(self.root1, width=self.root.winfo_screenwidth(),
                                                       height=self.root.winfo_screenheight())
        self.scroll.pack(pady=10)
        self.scroll.columnconfigure(0)
        self.mainRecipyFrame = Frame(self.scroll)
        self.mainRecipyFrame.pack(pady=10)
        self.f11 = Frame(self.mainRecipyFrame,width=self.root1.winfo_screenwidth()/3)
        self.f11.grid(row=0, column=0, pady=10, padx=10)

        img = Image.open(fp=recipy[-1])
        print(img)
        img = img.resize((400, 400))
        imgTk = ImageTk.PhotoImage(image=img)
        self.l1 = Label(self.f11, image=imgTk)
        self.l1.image = imgTk
        self.l1.pack(expand=True,fill="both")

        self.f2 = Frame(self.mainRecipyFrame,width=self.scroll.winfo_screenwidth())
        self.f2.grid(row=0,column=1,pady=10,padx=10)

        self.name = Label(self.f2, text=f"Recipe Name- {recipy[1]}", font=('',16))
        self.name.grid(row=0,column=0,pady=10,padx=10)

        self.cat = Label(self.f2, text=f"Category- {recipy[5]}", font=('', 16))
        self.cat.grid(row=1, column=0, pady=10, padx=10)

        self.dur = Label(self.f2, text=f'Duration(in min)- {recipy[3]}', font=('', 16))
        self.dur.grid(row=2, column=0, pady=10, padx=10)

        self.ing = Label(self.f2, text=f'Ingredients- {recipy[4]}', font=('', 16),wraplength=1000)
        self.ing.grid(row=3, column=0, pady=10, padx=10)

        self.des = Label(self.f2, text=f'Description- {recipy[2]}', font=('', 16),wraplength=1000)
        self.des.grid(row=4, column=0, pady=10, padx=10)

        self.button = Button(self.f2, text='Play',font=('',14,'bold'),width=8,
                             command=lambda :threading.Thread(target=self.playText, args=[recipy]).start())
        self.button.grid(row=5,column=0, pady=20)

        self.f3 = Frame(self.scroll)
        self.f3.pack()
        self.id = Label(self.f3,text="User ID", font=('',16,'bold'))
        self.id.grid(row=1,column=1,pady=10,padx=10)
        self.e1 = Entry(self.f3, width=6)
        self.e1.grid(row=1,column=2,pady=10)
        self.e1.insert(0, self.userid)
        self.e1.configure(state='readonly')

        self.ratings = Label(self.f3, text="Ratings", font=('', 16, 'bold'))
        self.ratings.grid(row=1, column=3, pady=10, padx=10)
        self.e2 = ttk.Combobox(self.f3, width=10, values=["1","2","3","4","5"] , state = "readonly",font=('',14))
        self.e2.grid(row=1, column=4, pady=10, padx=10)

        self.review = Label(self.f3, text="Reviews", font=('', 16, 'bold'))
        self.review.grid(row=1, column=6, pady=10, padx=10)
        self.e3 = Text(self.f3, width=30, height=5)
        self.e3.grid(row=1, column=7, pady=10, padx=10)
        rid=recipy[0]

        self.b2 = Button(self.f3, text="SUBMIT", font=('',16),command=lambda:self.insert(rid))
        self.b2.grid(row=2, column=5, pady=10,padx=10)



    def insert(self,rid):
        id = self.e1.get()
        rate = self.e2.get()
        review = self.e3.get('1.0', 'end-1c')
        if id == '' or rate == '' or review == '':
            msg.showwarning("warning" , "please enter all values")
        else:
            conn = Connect()
            cr = conn.cursor()

            q = f"insert into ratings values(null, '{self.userid}','{rid}','{rate}','{review}')"

            cr.execute(q)
            conn.commit()
            msg.showwarning("success", "Review added")








    def playText(self,recipy):
        lst = os.listdir('.')

        if 'hello.mp3' in lst:
            os.remove('hello.mp3')

        obj = gTTS(text=recipy[2], lang='en')

        obj.save("hello.mp3")

        playsound.playsound('hello.mp3')

        os.remove('hello.mp3')

        self.root1.mainloop()
#obj = Main(8)


