from tkinter import *
import tkinter.messagebox as msg
import tkinter.ttk as ttk
import connection

class user:
    def __init__(self):
        self.mainlbcolour = "#CFCCD6"
        self.root = Tk()
        self.root.geometry("600x600")
        self.root.title("Add User")
        self.root.configure(bg="#AD9BAA")

        self.mainLabel = Label(self.root, text="Add User", font=('', 28, "bold"), bg=self.mainlbcolour, foreground="Black")
        self.mainLabel.pack(pady=20, ipadx=20, ipady=20)

        self.frames = Frame(self.root, bg="#CFCCD6")
        self.frames.pack()
        self.font = ('', 15)

        self.l1 = Label(self.frames, text="NAME", font=self.font, bg="#CFCCD6")
        self.e1 = Entry(self.frames, font= self.font, relief=SOLID)
        self.l1.grid(row=0, column=0, pady=15, padx=10)
        self.e1.grid(row=0, column=1, pady=15, padx=10)

        self.l2 = Label(self.frames, text="EMAIL", font=self.font, bg="#CFCCD6")
        self.e2 = Entry(self.frames, font=self.font, relief=SOLID)
        self.l2.grid(row=1, column=0, pady=15, padx=10)
        self.e2.grid(row=1, column=1, pady=15, padx=10)

        self.l3= Label(self.frames, text="MOBILE", font=self.font, bg="#CFCCD6")
        self.e3 = Entry(self.frames, font=self.font, relief=SOLID)
        self.l3.grid(row=2, column=0, pady=15, padx=10)
        self.e3.grid(row=2, column=1, pady=15, padx=10)

        self.l4 = Label(self.frames, text="PASSWORD", font=self.font, bg="#CFCCD6")
        self.e4 = Entry(self.frames, font=self.font, relief=SOLID)
        self.l4.grid(row=3, column=0, pady=15, padx=10)
        self.e4.grid(row=3, column=1, pady=15, padx=10)

        self.l5 = Label(self.frames, text="GENDER", font=self.font, bg="#CFCCD6")
        self.e5 = Entry(self.frames, font=self.font, relief=SOLID)
        self.l5.grid(row=4, column=0, pady=15, padx=10)
        self.e5.grid(row=4, column=1, pady=15, padx=10)

        self.l6 = Label(self.frames, text="ADDRESS", font=self.font, bg="#CFCCD6")
        self.e6 = Entry(self.frames, font=self.font, relief=SOLID)
        self.l6.grid(row=5, column=0, pady=15, padx=10)
        self.e6.grid(row=5, column=1, pady=15, padx=10)

        self.b1 = Button(self.root, text="SUBMIT", width= 25 ,font=18, command=self.submit,
                         highlightthickness=5, relief=RAISED)
        self.b1.pack(pady=20)

        self.root.mainloop()

    def submit(self):
            name = self.e1.get()
            email = self.e2.get()
            mobile = self.e3.get()
            password = self.e4.get()
            gender = self.e5.get()
            address = self.e6.get()
            if name == '' or email == '' or mobile == '' or password == '' or gender == '' or address == '':
                msg.showwarning("warning", "please enter all values")
            else:
                self.conn = connection.Connect()
                self.cr = self.conn.cursor()
                q = f"insert into user values(null,'{name}','{email}', '{mobile}','{password}','{gender}','{address}')"
                self.cr.execute(q)
                self.conn.commit()
                msg.showinfo("SUCCESS", "USER HAS BEEN ADDED")
if __name__ == '__main__':
    obj = user()




